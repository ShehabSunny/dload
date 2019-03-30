from urllib.request import urlparse, url2pathname
from os.path import basename

class Source():
    def __init__(self, url: str, download_dir: str, *args, **kwargs):
        self.url = url
        path = basename(self.url)
        self.file_name = url2pathname(path).rstrip()
        self.download_dir = download_dir

    def download(self):
        raise NotImplementedError("download function is not implemented")