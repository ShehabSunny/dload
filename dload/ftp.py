from tqdm import tqdm
from .source import Source
import os
from urllib.request import urlopen, Request
import math


class FtpSource(Source):
    def download(self):
        print(os.path.join(self.download_dir, self.file_name))
        print("downloading using ftp protocol")
        print(f"URL: {self.url}")

        req = Request(self.url)
        response = urlopen(req)
        CHUNK = 16 * 1024
        with open(os.path.join(self.download_dir, self.file_name), 'wb') as f:
            # for _ in tqdm(range(math.ceil(response.length / CHUNK))):
            while True:
                chunk = response.read(CHUNK)
                if not chunk:
                    break
                f.write(chunk)

