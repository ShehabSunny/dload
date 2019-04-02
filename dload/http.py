from .source import Source
import os
from urllib.request import urlopen, Request
import math
import tempfile
import shutil


class HttpSource(Source):
    def __init__(self, *args, **kwargs):
        super(HttpSource, self).__init__(*args, **kwargs)
        self._chunk_len = 16 * 1024
        # add headers to act like a broweser
        self._headers = {'User-Agent': 
            """
            Mozilla/5.0 (Windows NT 6.1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/41.0.2228.0 Safari/537.3
            """
        }

    def download(self):
        # create a temporary file
        temp, temp_path = tempfile.mkstemp()
        # download the file from url
        try:
            req = Request(self.url, headers=self._headers)
            response = urlopen(req)
            total = math.ceil(response.length / self._chunk_len)
            for downloaded in range(total):
                chunk = response.read(self._chunk_len)
                os.write(temp, chunk)
                print(f"Downloading: {round((downloaded/total)*100, 2)}%", end='\r')
            # move to destination
            print(f"Downloading: 100.0%", end='\r')
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            os.close(temp)
            os.remove(temp_path)