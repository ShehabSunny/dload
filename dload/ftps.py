from .source import Source
import ftplib
from urllib.parse import urlparse
import socket
import tempfile
import os
import shutil
import itertools


class FtpsSource(Source):
    def __init__(self, *args, **kwargs):
        super(FtpsSource, self).__init__(*args, **kwargs)
        self.ftps = ftplib.FTP_TLS()
        self.ftps.af = socket.AF_INET6
        self._fpts_path = "/".join(self.parsed_url.path.split("/")[:-1])
        self._chunk_len = 16 * 1024


    def _connect(self):
        try:
            # FTP_TLS init
            if self.port is None:
                port = 21 # default for FTPS
            else: 
                port = self.port
            msg = self.ftps.connect(self.host, port, timeout=self.timeout)
            return 0, msg
        except Exception as e:
            return -1, str(e)


    def _login(self):
        try:
            # login to server
            self.ftps.login(self.username, self.password)
            self.ftps.prot_p()
            return 0, ""
        except Exception as e:
            self.ftps.close()
            return -1, str(e)


    def _cwd(self):
        try:
            self.ftps.cwd(self._fpts_path)
            return 0, ""
        except Exception as e:
            self.ftps.close()
            return -1, str(e)


    def download(self):
        # connect to server
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

        #  create a temporary file
        temp, temp_path = tempfile.mkstemp()
    
        loader = itertools.cycle(["\\", "|", "/", "-"])
        # callback
        def cb(data):
            print(f"Downloading: {next(loader)}", end='\r')
            # store in temp file
            os.write(temp, data)

        try:
            # download and store into temp file
            self.ftps.retrbinary(cmd='RETR %s' % self.file_name, blocksize=self._chunk_len, callback=cb)
            # close and move to destination
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            self.ftps.close()
            os.close(temp)
            os.remove(temp_path)