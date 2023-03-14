# Importar el módulo unittest y el script Qr_generator.py
import unittest
import Qr_generator
import os
import qrcode
from PIL import Image
# Crear una clase de prueba que herede de unittest.TestCase
class TestQrGenerator(unittest.TestCase):

    # Definir métodos de prueba que comprueben el funcionamiento del código QR
    def test_folder_creation(self):
        # Comprobar que se crea la carpeta 'QR_image'
        self.assertTrue(os.path.exists('QR_image'))

    def test_qr_generation(self):
        # Comprobar que se generan los archivos QR para cada URL
        for url in Qr_generator.urls:
            self.assertTrue(os.path.exists(os.path.join('QR_image', url.replace('https://', '') + '.png')))

    def test_qr_data(self):
        # Comprobar que los datos del código QR coinciden con la URL
        for url in Qr_generator.urls:
            img = Image.open(os.path.join('QR_image', url.replace('https://', '') + '.png'))
            qr = qrcode.image.pil.PilImage(img, width=10, box_size=4)
            self.assertEqual(qr.data, url)

# Ejecutar el script de prueba con unittest.main()
if __name__ == '__main__':
    unittest.main()