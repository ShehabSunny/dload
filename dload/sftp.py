from .source import Source
import paramiko
from urllib.parse import urlparse
import tempfile
import os
import shutil


class SftpSource(Source):
    def __init__(self, *args, **kwargs):
        super(SftpSource, self).__init__(*args, **kwargs)
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self._sftp_path = self.parsed_url.path


    def _connect(self):
        """
        connect and login to SFTP server
        """
        try:
            if self.port is None:
                port = 22 # default for SFTP
            else: 
                port = self.port
            # connect to server
            self.ssh.connect(
                self.host, 
                port=port, 
                username=self.username, 
                password=self.password, 
                timeout=self.timeout, 
                allow_agent=False, 
                look_for_keys=False
            )
            self.sftp = self.ssh.open_sftp()
            return 0, ""
        except Exception as e:
            return -1, str(e)


    def download(self):
        """
        Download the file
        """
        # connect to server
        code, msg = self._connect()
        if code != 0:
            return code, msg

        # callback
        def cb(downloaded, total):
            print(f"Downloading: {(downloaded/total)*100}%", end='\r')

        # create a temporary file
        temp, temp_path = tempfile.mkstemp()

        try:
            # download
            self.sftp.get(self._sftp_path, temp_path, callback=cb)
            # move to destination
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            self.sftp.close()
            os.close(temp)
            os.remove(temp_path)