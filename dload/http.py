from tqdm import tqdm
from .source import Source
import os
from urllib.request import urlopen, Request
import math


class HttpSource(Source):
    def download(self):
        print(f"Location: {self.file_location}")

        # add headers to act like a broweser
        headers = {'User-Agent': 
            """
            Mozilla/5.0 (Windows NT 6.1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/41.0.2228.0 Safari/537.3
            """
        }

        req = Request(self.url, headers=headers)
        response = urlopen(req)
        chunk_len = 16 * 1024
        with open(self.file_location, 'wb') as f:
            for _ in tqdm(range(math.ceil(response.length / chunk_len))):
                chunk = response.read(chunk_len)
                f.write(chunk)
