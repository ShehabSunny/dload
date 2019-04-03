import unittest
from .sftp import SftpSource
import tempfile

class TestSftp(unittest.TestCase):
    test_urls = [
        # Sftp
        "sftp://demo:password@test.rebex.net:22/readme.txt",
        "sftp://demo:password@test.rebex.net/readme.txt",
        # Scp Protocol
        "scp://demo:password@test.rebex.net:22/pub/example/FtpDownloader.png",
        "scp://demo:password@test.rebex.net/pub/example/FtpDownloader.png",
        # SSH protocol
        "ssh://demo:password@test.rebex.net/readme.txt",
        "ssh://demo:password@test.rebex.net:22/readme.txt"
    ]

    wrong_urls = [
        "sftp://:password@test.rebex.net:22/readme.txt",
        "sftp://demo:@test.rebex.net:22/readme.txt",
        "sftp://test.rebex.net:22/readme.txt",
        "sftp://test.rebex.net:22/readme.txt", # no email pass
        # Scp Protocol
        "scp://:password@test.rebex.net:22/pub/example/FtpDownloader.png",
        "scp://demo:@test.rebex.net/pub/example/FtpDownloader.png",
        "scp://@test.rebex.net/pub/example/FtpDownloader.png", # no email pass
        # SSH protocol
        "ssh://:password@test.rebex.net/readme.txt",
        "ssh://demo:@test.rebex.net:22/readme.txt",
        "ssh://@test.rebex.net:22/readme.txt" # no email pass
    ]

    def test_create(self):
        """
        Test initalization
        """
        for url in TestSftp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                sftp = SftpSource(url, tmpdirname)
                self.assertEqual(sftp.url, url)

    def test_connect(self):
        """
        Test connect to server
        """
        for url in TestSftp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                sftp = SftpSource(url, tmpdirname)
                code, _ = sftp._connect()
                self.assertEqual(code, 0)


    def test_download(self):
        """
        Test download
        """
        for url in TestSftp.test_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                sftp = SftpSource(url, tmpdirname)
                code, _ = sftp.download()
                self.assertEqual(code, 0)

    def test_wrong_url(self):
        """
        Test using a wrong url
        """
        for url in TestSftp.wrong_urls:
            with tempfile.TemporaryDirectory() as tmpdirname:
                http = SftpSource(url, tmpdirname)
                code, _ = http.download()
                self.assertNotEqual(code, 0)

if __name__ == '__main__':
    unittest.main()
