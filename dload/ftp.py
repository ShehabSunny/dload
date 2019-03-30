from .source import Source

class FtpSource(Source):
    def download(self):
        print("downloading using ftp protocol")
        print(f"URL: {self.url}")