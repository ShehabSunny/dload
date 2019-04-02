import unittest
from .ftps import FtpsSource
import tempfile

class TestFtps(unittest.TestCase):
    demo_url = "ftps://demo:password@test.rebex.net:22/readme.txt"

    def test_create(self):
        """
        Test initalization
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftps = FtpsSource(TestFtps.demo_url, tmpdirname)
            self.assertEqual(ftps.url, TestFtps.demo_url)

    def test_connect(self):
        """
        Test connect
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftps = FtpsSource(TestFtps.demo_url, tmpdirname)
            code, _ = ftps._connect()
            self.assertEqual(code, 0)

    def test_login(self):
        """
        Test login
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftps = FtpsSource(TestFtps.demo_url, tmpdirname)
            code, _ = ftps._connect()
            code, _ = ftps._login()
            self.assertEqual(code, 0)

    def test_cwd(self):
        """
        Test change directory
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftps = FtpsSource(TestFtps.demo_url, tmpdirname)
            code, _ = ftps._connect()
            code, _ = ftps._login()
            code, _ = ftps._cwd()
            self.assertEqual(code, 0)

    def test_download(self):
        """
        Test download
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            ftps = FtpsSource(TestFtps.demo_url, tmpdirname)
            code, _ = ftps.download()
            self.assertEqual(code, 0)


if __name__ == '__main__':
    unittest.main()
