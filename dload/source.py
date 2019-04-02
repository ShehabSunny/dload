from urllib.request import urlparse, url2pathname
from os.path import basename
import os

class Source():
    """
    Inherit from this class for each different protocol implementations.
    """
    def __init__(self, url: str, download_dir: str, timeout=60, *args, **kwargs):
        self.url = url
        path = basename(self.url)
        self.file_name = url2pathname(path).rstrip()
        self.download_dir = download_dir
        self.file_location = os.path.join(self.download_dir, self.file_name)
        self.timeout = timeout
        # parse url 
        self.parsed_url = urlparse(self.url)
        self.username = self.parsed_url.username
        self.password = self.parsed_url.password
        self.host = self.parsed_url.hostname
        self.port = self.parsed_url.port


    def download(self):
        """
        download function is implemented by all the subclasses.
        it should implement how to download using a particular protocol.
        all the temporary files created should delete while exiting.
        """
        raise NotImplementedError("download function is not implemented")