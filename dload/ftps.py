from .source import Source
import ftplib
from urllib.parse import urlparse
import socket
import tempfile
import os
import shutil


class FtpsSource(Source):
    def download(self):
        # parse url 
        u = urlparse(self.url)
        host = u.hostname
        port = u.port
        if port is None:
            port = 21 #default port for FTPS
        username = u.username
        password = u.password
        path = "/".join(u.path.split("/")[:-1])
        # define chunk size
        chunk_len = 16 * 1024
        
        # FTP_TLS init
        ftps = ftplib.FTP_TLS()
        ftps.af = socket.AF_INET6

        # connect to server
        try:
            ftps.connect(host, port)
        except Exception as e:
            return -1, str(e)
        
        # login
        try:
            ftps.login(username, password)
            ftps.prot_p()
        except Exception as e:
            ftps.close()
            return -1, str(e)

        # chane directory
        try:
            ftps.cwd(path)
        except Exception as e:
            ftps.close()
            return -1, str(e)

         # create a temporary file
        temp, temp_path = tempfile.mkstemp()
    
        # callback
        def cb(data):
            print(".", end="")
            # store in temp file
            os.write(temp, data)

        try:
            # download and store into temp file
            ftps.retrbinary(cmd='RETR %s' % self.file_name, blocksize=chunk_len, callback=cb)
            # close and move to destination
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            ftps.close()
            os.close(temp)
            os.remove(temp_path)