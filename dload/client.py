from .http import HttpSource
from .ftp import FtpSource
from .ftps import FtpsSource
from .sftp import SftpSource
from .ssh import SshSource
from .common import parse_protocol
import sys


class Client():
    """
    Entrypoint for file download.
    Simple usecase:
        client = Client(download_location:str, timeout=60)
        client.download(url:str)
    """
    def __init__(self, download_dir, timeout=60):
        self._download_dir = download_dir
        self.timeout = timeout

    def download(self, url: str):
        """
        handle all protocols here
        """
        protocol = parse_protocol(url)
        print(f"URL: {url}")
        print(f"Protocol: {protocol}")
        if protocol == 'http':
            source = HttpSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'https':
            source = HttpSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'ftp':
            source = FtpSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'ftps':
            source = FtpsSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'sftp':
            source = SshSource(url, self._download_dir, timeout=self.timeout)# use SSH for SFTP
        elif protocol == 'ssh':
            source = SshSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'scp':
            source = SshSource(url, self._download_dir, timeout=self.timeout)# use SSH for SCP
        else:
            print(f"protocol {protocol} is not supported yet", file=sys.stderr)
            return -1
        # download the file
        try:
            res_code, err_msg = source.download()
            if res_code == 0:
                print("\n\U0001F44D Download successful\n")
            else:
                print(f"\U0001F44E Download failed: {err_msg}\n", file=sys.stderr)
        except Exception as ex:
            print(f"\U0001F44E Download failed: {str(ex)}\n")

