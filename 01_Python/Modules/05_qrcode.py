import qrcode
data = "Aditya Yadav is the greatest daddy of all time"
img = qrcode.make(data)
img.show()
img.save("plain_text_qr.png") 