import unittest
from .ftps import FtpsSource
import tempfile

class TestFtps(unittest.TestCase):
    test_urls = [
        "ftps://demo:password@test.rebex.net:21/readme.txt",
        "ftps://demo:password@test.rebex.net/readme.txt"
    ]

    wrong_urls = [
        "ftps://:password@test.rebex.net:21/readme.txt",
        "ftps://demo:@test.rebex.net:21/readme.txt",
        "ftps://test.rebex.net:21/readme.txt" # no username pass
    ]

    def test_create(self):
        """
        Test initalization
        """
        for url in TestFtps.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftps = FtpsSource(url, tmpdirname)
                self.assertEqual(ftps.url, url)

    def test_connect(self):
        """
        Test connect
        """
        for url in TestFtps.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftps = FtpsSource(url, tmpdirname)
                code, _ = ftps._connect()
                self.assertEqual(code, 0)

    def test_login(self):
        """
        Test login
        """
        for url in TestFtps.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftps = FtpsSource(url, tmpdirname)
                code, _ = ftps._connect()
                code, _ = ftps._login()
                self.assertEqual(code, 0)

    def test_cwd(self):
        """
        Test change directory
        """
        for url in TestFtps.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftps = FtpsSource(url, tmpdirname)
                code, _ = ftps._connect()
                code, _ = ftps._login()
                code, _ = ftps._cwd()
                self.assertEqual(code, 0)

    def test_download(self):
        """
        Test download
        """
        for url in TestFtps.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                ftps = FtpsSource(url, tmpdirname)
                code, _ = ftps.download()
                self.assertEqual(code, 0)

    def test_wrong_url(self):
        """
        Test using a wrong url
        """
        for url in TestFtps.wrong_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                http = FtpsSource(url, tmpdirname)
                code, _ = http.download()
                self.assertNotEqual(code, 0)


if __name__ == '__main__':
    unittest.main()
