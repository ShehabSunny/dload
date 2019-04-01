from .source import Source
import ftplib
from urllib.parse import urlparse


class FtpSource(Source):
    def download(self):
        # parse url 
        u = urlparse(self.url)
        host = u.hostname
        port = u.port
        username = u.username
        password = u.password
        path = "/".join(u.path.split("/")[:-1])
        # define chunk size
        chunk_len = 16 * 1024
        
        # FTP init
        ftp = ftplib.FTP()

        # connect to server
        try:
            ftp.connect(host, port)
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

        # define file handler
        handler = open(self.file_location, 'wb')
        # download
        try:
            ftp.retrbinary(cmd='RETR %s' % self.file_name, blocksize=chunk_len, callback=handler.write)
            ftp.close()
            return 0, ""
        except ftplib.error_perm as ex:
            ftp.close()
            return -1, str(ex)
