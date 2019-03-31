from tqdm import tqdm
from .source import Source
import os
from urllib.request import urlopen, Request
import time
import itertools


class FtpsSource(Source):
    def download(self):
        print(f"Location: {self.file_location}")

        req = Request(self.url)
        response = urlopen(req)
        chunk_len = 16 * 1024
        print('Downloading', end='')
        with open(self.file_location, 'wb') as f:
            for c in itertools.count():
                if c % 40 == 0:
                    print(".", end ="")
                chunk = response.read(chunk_len)
                if not chunk:
                    break
                f.write(chunk)
        print('\n')

