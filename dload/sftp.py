from .source import Source
import paramiko
from urllib.parse import urlparse


class SftpSource(Source):
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
        
        # init client
        transport = paramiko.Transport((host, port))
        sftp = paramiko.SFTPClient.from_transport(transport)

        # connect to server
        try:
            ftps.connect(host, port)
        except Exception as e:
            return -1, str(e)
        
        # login
        try:
            ftps.login(username, password)
            ftps.prot_p()
            ftps.nlst()
        except Exception as e:
            ftps.close()
            return -1, str(e)

        # chane directory
        try:
            ftps.cwd(path)
        except Exception as e:
            ftps.close()
            return -1, str(e)

        # define file handler
        handler = open(self.file_location, 'wb')
        # download
        try:
            ftps.retrbinary(cmd='RETR %s' % self.file_name, blocksize=chunk_len, callback=handler.write)
            ftps.close()
            return 0, ""
        except ftplib.error_perm as ex:
            ftps.close()
            return -1, str(ex)
