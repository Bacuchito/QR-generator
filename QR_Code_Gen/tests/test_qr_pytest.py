import pytest
from QR_Code_Gen.Qr_generator import crear_qr
import os
from urllib.parse import urlparse


def test_crear_qr():
    """Test that the qr_generator"""
    urls = ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com"]
    crear_qr(urls)

    for url in urls:
        sitio_web = urlparse(url).hostname
        assert os.path.exists(f"qr_image/{sitio_web}.png")

    for url in urls:
        sitio_web = urlparse(url).hostname
        os.remove(f"qr_image/{sitio_web}.png")

