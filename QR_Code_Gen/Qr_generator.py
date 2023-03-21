import os
import qrcode
from urllib.parse import urlparse

def crear_qr(urls):
    if not os.path.exists("qr_image"):
        os.makedirs("qr_image")
    

    for url in urls:
        sitio_web = urlparse(url).hostname
        img = qrcode.make(url)
        img.save(f"qr_image/{sitio_web}.png")

urls = ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com"]
crear_qr(urls)
