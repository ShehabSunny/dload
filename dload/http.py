from .source import Source

class HttpSource(Source):
    def download(self):
        print("downloading using http protocol")
        print(f"URL: {self.url}")
