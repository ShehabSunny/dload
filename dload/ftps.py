from .source import Source
import ftplib
from urllib.parse import urlparse
import sys


class FtpsSource(Source):
    def download(self):
        print(f"Location: {self.file_location}")

        # parse url 
        u = urlparse(self.url)
        host = u.hostname
        port = u.port
        username = u.username
        password = u.password
        path = "/".join(u.path.split("/")[:-1])
        # define chunk size
        chunk_len = 16 * 1024
        
        # FTP_TLS init
        ftps = ftplib.FTP_TLS()

        # connect to server
        try:
            ftps.connect(host, port)
        except Exception as e:
            print(f"could not connect to server: {str(e)}")
            return
        
        # login
        try:
            ftps.login(username, password)
            ftps.prot_p()
            ftps.nlst()
        except Exception as e:
            print(f"could not login to server: {str(e)}")
            ftps.close()
            return

        # chane directory
        try:
            ftps.cwd(path)
        except Exception as e:
            print(f"ftps file path is not valid: {str(e)}")
            ftps.close()
            return

        # define file handler
        handler = open(self.file_location, 'wb')
        # download
        try:
            ftps.retrbinary(cmd='RETR %s' % self.file_name, blocksize=chunk_len, callback=handler.write)
        except ftplib.error_perm as ex:
            print(f"could not download the file: {str(ex)}\n", file=sys.stderr)
        finally: 
            ftps.close()
            return
