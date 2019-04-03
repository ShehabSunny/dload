import unittest
from .http import HttpSource
import tempfile

class TestHttp(unittest.TestCase):
    test_urls = [
        "https://www.rust-lang.org/static/images/twitter.svg",
        "http://www.africau.edu/images/default/sample.pdf"
    ]
    wrong_urls = [
        "http://www.example.fake/image/file.pdf"
    ]

    def test_create_https(self):
        """
        Test initalization
        """
        for url in TestHttp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                http = HttpSource(url, tmpdirname)
                self.assertEqual(http.url, url)

    
    def test_download_http(self):
        """
        Test download
        """
        for url in TestHttp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                http = HttpSource(url, tmpdirname)
                code, _ = http.download()
                self.assertEqual(code, 0)

    def test_wrong_url(self):
        """
        Test using a wrong url
        """
        for url in TestHttp.wrong_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                http = HttpSource(url, tmpdirname)
                code, err_msg = http.download()
                self.assertNotEqual(code, 0)
                self.assertIn("getaddrinfo failed", err_msg)





if __name__ == '__main__':
    unittest.main()
