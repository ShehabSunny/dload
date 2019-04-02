from .source import Source
import paramiko
from urllib.parse import urlparse
import tempfile
import os
import shutil


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
            ssh.connect(host, port=port, username=username, password=password, timeout=self.timeout, allow_agent=False, look_for_keys=False)
            sftp = ssh.open_sftp()
        except Exception as e:
            return -1, str(e)

        # callback
        def cb(downloaded, total):
            print(f"Downloading: {(downloaded/total)*100}%", end='\r')

        # create a temporary file
        temp, temp_path = tempfile.mkstemp()

        try:
            # download
            sftp.get(path, temp_path, callback=cb)
            # move to destination
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            sftp.close()
            os.close(temp)
            os.remove(temp_path)