import qrcode
import os
# list of URL
urls = ['https://www.bing.com', 'https://www.google.com', 'https://www.yahoo.com']
# name of the folder
folder = 'QR_image'



'''QR code generator script'''
if not os.path.exists(folder):
    os.mkdir(folder)

for i, url in enumerate(urls):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
  
    qr.add_data(url)
    qr.make(fit=True)
    # Save the qr in the folder
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(folder, url.replace('https://', '') + '.png'))