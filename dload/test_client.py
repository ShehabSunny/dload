import unittest
from .client import Client
import tempfile

class TestClient(unittest.TestCase):
    def test_create_client(self):
        """
        Test client initalization
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            c = Client(download_dir=tmpdirname)
            self.assertIsInstance(c, Client)


    def test_download_fake_protocol(self):
        """
        Test client initalization
        """
        with tempfile.TemporaryDirectory() as tmpdirname:
            c = Client(download_dir=tmpdirname)
            res_code, err_msg = c.download("fake://example.com/file")
            self.assertEqual(res_code, -1)  
            self.assertEqual(err_msg, "protocol fake is not supported yet") 


    def test_get_protocol(self):
        """
        Test client protocol parse
        """
        protocol = Client.get_protocol("https://example.com")
        self.assertEqual(protocol, "https") 
        protocol = Client.get_protocol("ftp://example.com")
        self.assertEqual(protocol, "ftp")  
              


if __name__ == '__main__':
    unittest.main()
