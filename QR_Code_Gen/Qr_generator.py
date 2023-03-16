import os
import qrcode
from urllib.parse import urlparse

def crear_qr(urls):
    # Crear carpeta para almacenar las imágenes QR
    if not os.path.exists("qr_image"):
        os.makedirs("qr_image")
    
    # Crear código QR para cada URL y guardar la imagen
    for url in urls:
        # Obtener el nombre del sitio web de la URL
        sitio_web = urlparse(url).hostname
        # Crear el código QR y guardarlo con el nombre del sitio web
        img = qrcode.make(url)
        img.save(f"qr_image/{sitio_web}.png")

urls = ["https://www.google.com", "https://www.facebook.com", "https://www.twitter.com"]
crear_qr(urls)
