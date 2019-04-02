from .source import Source
import ftplib
from urllib.parse import urlparse
import tempfile
import os
import shutil
import itertools


class FtpSource(Source):
    def download(self):
        # parse url 
        u = urlparse(self.url)
        host = u.hostname
        port = u.port
        if port is None:
            port = 21 #default port for FTP
        username = u.username
        password = u.password
        path = "/".join(u.path.split("/")[:-1])
        # define chunk size
        chunk_len = 16 * 1024
        
        # FTP init
        ftp = ftplib.FTP()

        # connect to server
        try:
            ftp.connect(host, port, timeout=self.timeout)
        except Exception as e:
            return -1, str(e)
        
        # login
        try:
            ftp.login(username, password)
        except Exception as e:
            ftp.close()
            return -1, str(e)

        # change directory
        try:
            ftp.cwd(path)
        except Exception as e:
            ftp.close()
            return -1, str(e)

        # create a temporary file
        temp, temp_path = tempfile.mkstemp()
    
        loader = itertools.cycle(["\\", "|", "/", "-"]) 
        # callback
        def cb(data):
            print(f"Downloading: {next(loader)}", end='\r')
            # store in temp file
            os.write(temp, data)
            
        try:
            # download and write into temporary file
            ftp.retrbinary(cmd='RETR %s' % self.file_name, blocksize=chunk_len, callback=cb)
            # close and move to destination
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            ftp.close()
            os.close(temp)
            os.remove(temp_path)
