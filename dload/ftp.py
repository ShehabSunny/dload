from .source import Source
import ftplib
from urllib.parse import urlparse
import tempfile
import os
import shutil
import itertools


class FtpSource(Source):
    def __init__(self, *args, **kwargs):
        super(FtpSource, self).__init__(*args, **kwargs)
        self.ftp = ftplib.FTP()
        self._fpt_path = "/".join(self.parsed_url.path.split("/")[:-1])
        self._chunk_len = 16 * 1024


    def _connect(self):
        try:
            # connect to server
            if self.port is None:
                port = 21 # default for FTP
            else: 
                port = self.port
            self.ftp.connect(self.host, port, timeout=self.timeout)
            return 0, ""
        except Exception as e:
            return -1, str(e)


    def _login(self):
        try:
            self.ftp.login(self.username, self.password)
            return 0, ""
        except Exception as e:
            self.ftp.close()
            return -1, str(e)


    def _cwd(self):
        try:
            self.ftp.cwd(self._fpt_path)
            return 0, ""
        except Exception as e:
            self.ftp.close()
            return -1, str(e)



    def download(self):
        # connect
        code, msg = self._connect()
        if code != 0:
            return code, msg

        # login
        code, msg = self._login()
        if code != 0:
            return code, msg

        # change directory
        code, msg = self._cwd()
        if code != 0:
            return code, msg

        # create a temporary file
        temp, temp_path = tempfile.mkstemp()
        # loader
        loader = itertools.cycle(["\\", "|", "/", "-"]) 
        # callback
        def cb(data):
            print(f"Downloading: {next(loader)}", end='\r')
            # store in temp file
            os.write(temp, data)
            
        try:
            # download and write into temporary file
            self.ftp.retrbinary(cmd='RETR %s' % self.file_name, blocksize=self._chunk_len, callback=cb)
            # close and move to destination
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            self.ftp.close()
            os.close(temp)
            os.remove(temp_path)
