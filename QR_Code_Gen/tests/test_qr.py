from QR_Code_Gen.Qr_generator import crear_qr
import os
import unittest


class TestQRGenerator(unittest.TestCase):
    
    def test_crear_qr(self):
        """Create a qr code and verify"""
        urls = ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com"]
        crear_qr(urls)
        self.assertTrue(os.path.exists("qr_image/www.google.com.png"))
        self.assertTrue(os.path.exists("qr_image/www.facebook.com.png"))
        self.assertTrue(os.path.exists("qr_image/www.twitter.com.png"))

    def tearDown(self):
        if os.path.exists("qr_image"):
            for archivo in os.listdir("qr_image"):
                archivo_path = os.path.join("qr_image", archivo)
                os.remove(archivo_path)
            os.rmdir("qr_image")
        
if __name__ == '__main__':
    unittest.main()
