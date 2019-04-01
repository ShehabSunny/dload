from .source import Source
import paramiko
from urllib.parse import urlparse


class SshSource(Source):
    def download(self):
        # parse url 
        u = urlparse(self.url)
        host = u.hostname
        port = u.port
        if port is None:
            port = 22 # default port for ssh
        username = u.username
        password = 'password' #u.password
        path = u.path
        # define chunk size
        chunk_len = 16 * 1024
        

        # init client
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            # connect to server
            print(port, username, password)
            ssh.connect(host, port=port, username=username, password=password, allow_agent=False, look_for_keys=False)
            sftp = ssh.open_sftp()
        except Exception as e:
            return -1, str(e)

        # callback
        def cb(downloaded, total):
            print(".", end='')

        # download
        try:
            sftp.get(path, self.file_location, callback=cb)
            sftp.close()
            return 0, ""
        except Exception as ex:
            sftp.close()
            return -1, str(ex)
