import qrcode as qr

def QR_maker(data):
    qr_code = qr.QRCode(version = 1, box_size = 10, border = 5)
    qr_code.add_data(data)
    qr_code.make(fit = True)
    pic = qr_code.make_image()
    pic.save('qrcode.png')
    print("QR generate is successful!")


data = "I am Rakib"
QR_maker(data)
