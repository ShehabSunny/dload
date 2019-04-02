import unittest
from .http import HttpSource
import tempfile

class TestHttp(unittest.TestCase):
    demo_https_url = "https://www.rust-lang.org/static/images/twitter.svg"
    demo_http_url = "http://www.africau.edu/images/default/sample.pdf"

    def test_create_https(self):
        """
        Test initalization
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = HttpSource(TestHttp.demo_http_url, tmpdirname)
            self.assertEqual(ftp.url, TestHttp.demo_http_url)

    def test_create_http(self):
        """
        Test initalization
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = HttpSource(TestHttp.demo_https_url, tmpdirname)
            self.assertEqual(ftp.url, TestHttp.demo_https_url)

    def test_download_https(self):
        """
        Test download
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = HttpSource(TestHttp.demo_https_url, tmpdirname)
            code, _ = ftp.download()
            self.assertEqual(code, 0)

    def test_download_http(self):
        """
        Test download
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = HttpSource(TestHttp.demo_http_url, tmpdirname)
            code, msg = ftp.download()
            print(msg)
            self.assertEqual(code, 0)


if __name__ == '__main__':
    unittest.main()
