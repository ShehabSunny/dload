from tqdm import tqdm
from .source import Source
import os
from urllib.request import urlopen, Request
import math


class HttpSource(Source):
    def download(self):
        print("downloading using http protocol")
        print(f"URL: {self.url}")

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

        req = Request(self.url, headers=headers)
        response = urlopen(req)
        CHUNK = 16 * 1024
        with open(os.path.join(self.download_dir, self.file_name), 'wb') as f:
            for _ in tqdm(range(math.ceil(response.length / CHUNK))):
                chunk = response.read(CHUNK)
                if not chunk:
                    break
                f.write(chunk)
