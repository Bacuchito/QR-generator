import pytest
from QR_Code_Gen.Qr_generator import crear_qr
import os
from urllib.parse import urlparse


def test_crear_qr():
    # Definir las URLs a probar
    urls = ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com"]

    # Ejecutar la función a probar
    crear_qr(urls)

    # Verificar que se hayan creado los códigos QR para cada URL
    for url in urls:
        sitio_web = urlparse(url).hostname
        assert os.path.exists(f"qr_image/{sitio_web}.png")

    # Borrar los códigos QR generados
    for url in urls:
        sitio_web = urlparse(url).hostname
        os.remove(f"qr_image/{sitio_web}.png")

