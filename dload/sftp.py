from .source import Source
import paramiko
from urllib.parse import urlparse


class SftpSource(Source):
    def download(self):
        # parse url 
        u = urlparse(self.url)
        host = u.hostname
        port = u.port
        if port is None:
            port = 22 # default port for sftp
        username = u.username
        password = u.password
        path = u.path
        # define chunk size
        chunk_len = 16 * 1024
        

        # open transport
        try:
            transport = paramiko.Transport((host, port))
        except Exception as e:
            return -1, f"could open transport: {str(e)}"
        
        # authenticate and get client
        try:
            transport.connect(username=username, password=password)
            sftp = paramiko.SFTPClient.from_transport(transport)
        except Exception as e:
            return -1, f"could not authenticate: {str(e)}"

        # callback
        def cb(downloaded, total):
            print(".", end='')

        # download
        try:
            sftp.get(path, self.file_location, callback=cb)
            sftp.close()
            transport.close()
            return 0, ""
        except Exception as ex:
            sftp.close()
            transport.close()
            return -1, str(ex)
