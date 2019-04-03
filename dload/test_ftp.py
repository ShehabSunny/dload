import unittest
from .ftp import FtpSource
import tempfile

class TestFtp(unittest.TestCase):
    test_urls = [
        "ftp://demo:password@test.rebex.net:21/readme.txt",
        "ftp://demo:password@test.rebex.net/readme.txt",
        "ftp://speedtest.tele2.net/1KB.zip"
    ]

    wrong_urls = [
        "ftp://:password@test.rebex.net:21/readme.txt",
        "ftp://demo:@test.rebex.net:21/readme.txt",
        "ftp://test.rebex.net:21/readme.txt",
        "ftp://test.rebex.net:21/readme.txt",
    ]

    def test_create(self):
        """
        Test initalization
        """
        for url in TestFtp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftp = FtpSource(url, tmpdirname)
                self.assertEqual(ftp.url, url)

    def test_connect(self):
        """
        Test connect
        """
        for url in TestFtp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftp = FtpSource(url, tmpdirname)
                code, _ = ftp._connect()
                self.assertEqual(code, 0)

    def test_login(self):
        """
        Test login
        """
        for url in TestFtp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftp = FtpSource(url, tmpdirname)
                code, _ = ftp._connect()
                code, _ = ftp._login()
                self.assertEqual(code, 0)

    def test_cwd(self):
        """
        Test change directory
        """
        for url in TestFtp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftp = FtpSource(url, tmpdirname)
                code, _ = ftp._connect()
                code, _ = ftp._login()
                code, _ = ftp._cwd()
                self.assertEqual(code, 0)

    def test_download(self):
        """
        Test download
        """
        for url in TestFtp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftp = FtpSource(url, tmpdirname)
                code, _ = ftp.download()
                self.assertEqual(code, 0)

    
    def test_wrong_url(self):
        """
        Test using a wrong url
        """
        for url in TestFtp.wrong_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                http = FtpSource(url, tmpdirname)
                code, _ = http.download()
                self.assertNotEqual(code, 0)

if __name__ == '__main__':
    unittest.main()
