from .http import HttpSource
from .ftp import FtpSource
from .ftps import FtpsSource
from .common import parse_protocol
import sys


class Client():
    def __init__(self, download_dir):
        self._download_dir = download_dir

    def download(self, url: str):
        """
        handle all protocols here
        """
        protocol = parse_protocol(url)
        print(f"URL: {url}")
        print(f"Protocol: {protocol}")
        if protocol == 'http':
            source = HttpSource(url, self._download_dir)
        elif protocol == 'https':
            source = HttpSource(url, self._download_dir)
        elif protocol == 'ftp':
            source = FtpSource(url, self._download_dir)
        elif protocol == 'ftps':
            source = FtpsSource(url, self._download_dir)
        else:
            print(f"protocol {protocol} is not supported yet", file=sys.stderr)
            return -1
        # download the file
        try:
            res_code, err_msg = source.download()
            if res_code == 0:
                print("Download successful\n")
            else:
                print(f"Download failed: {err_msg}\n", file=sys.stderr)
        except Exception as ex:
            print(f"Download failed: {str(ex)}\n")

