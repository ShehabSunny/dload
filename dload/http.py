from tqdm import tqdm
from .source import Source
import os
from urllib.request import urlopen, Request
import math
import tempfile
import shutil


class HttpSource(Source):
    def download(self):
        # add headers to act like a broweser
        headers = {'User-Agent': 
            """
            Mozilla/5.0 (Windows NT 6.1) \
            AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/41.0.2228.0 Safari/537.3
            """
        }
        # create a temporary file
        temp, temp_path = tempfile.mkstemp()
        
        # download
        try:
            req = Request(self.url, headers=headers)
            response = urlopen(req)
            chunk_len = 16 * 1024
            for _ in tqdm(range(math.ceil(response.length / chunk_len))):
                chunk = response.read(chunk_len)
                os.write(temp, chunk)
            # move to destination
            shutil.copy(temp_path, self.file_location)
            return 0, ""
        except Exception as ex:
            return -1, str(ex)
        finally:
            os.close(temp)
            os.remove(temp_path)