from .http import HttpSource
from .ftp import FtpSource
from .ftps import FtpsSource
from .sftp import SftpSource
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

    @staticmethod
    def get_protocol(url):
        return parse_protocol(url)

    def download(self, url: str):
        """
        handle all protocols here
        """
        protocol = Client.get_protocol(url)
        
        if protocol == 'http':
            source = HttpSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'https':
            source = HttpSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'ftp':
            source = FtpSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'ftps':
            source = FtpsSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'sftp':
            source = SftpSource(url, self._download_dir, timeout=self.timeout)
        elif protocol == 'ssh':
            source = SftpSource(url, self._download_dir, timeout=self.timeout) # use SFTP for SSH
        elif protocol == 'scp':
            source = SftpSource(url, self._download_dir, timeout=self.timeout)# use SFTP for SCP
        else:
            return -1, f"protocol {protocol} is not supported yet"
        # download the file
        try:
            res_code, err_msg = source.download()
            if res_code == 0:
                return 0, ""
            else:
                return res_code, err_msg
        except Exception as ex:
            return -1, str(ex)

