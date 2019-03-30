from .http import HttpSource
from .ftp import FtpSource
from .common import parse_protocol
import sys


class Client():
    @staticmethod
    def download(url: str, download_dir: str):
        protocol = parse_protocol(url)
        print(protocol)
        if protocol == 'http':
            source = HttpSource(url, download_dir)
        elif protocol == 'https':
            source = HttpSource(url, download_dir)
        elif protocol == 'ftp':
            print("here")
            source = FtpSource(url, download_dir)
        else:
            print(f"protocol {protocol} is not supported yet", file=sys.stderr)
            return
        # download the file
        source.download()
