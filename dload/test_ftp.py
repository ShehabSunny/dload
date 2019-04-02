import unittest
from .ftp import FtpSource
import tempfile

class TestFtp(unittest.TestCase):
    demo_url = "ftp://demo:password@test.rebex.net:21/readme.txt"

    def test_create(self):
        """
        Test initalization
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = FtpSource(TestFtp.demo_url, tmpdirname)
            self.assertEqual(ftp.url, TestFtp.demo_url)

    def test_connect(self):
        """
        Test connect
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = FtpSource(TestFtp.demo_url, tmpdirname)
            code, _ = ftp._connect()
            self.assertEqual(code, 0)

    def test_login(self):
        """
        Test login
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = FtpSource(TestFtp.demo_url, tmpdirname)
            code, _ = ftp._connect()
            code, _ = ftp._login()
            self.assertEqual(code, 0)

    def test_cwd(self):
        """
        Test change directory
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = FtpSource(TestFtp.demo_url, tmpdirname)
            code, _ = ftp._connect()
            code, _ = ftp._login()
            code, _ = ftp._cwd()
            self.assertEqual(code, 0)

    def test_download(self):
        """
        Test download
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftp = FtpSource(TestFtp.demo_url, tmpdirname)
            code, _ = ftp.download()
            self.assertEqual(code, 0)


if __name__ == '__main__':
    unittest.main()
