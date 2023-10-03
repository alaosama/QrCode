import pyqrcode
import png 

url = input("Enter a URL to generate QR Code : ")

QR = pyqrcode.create(url)

QR.png("webqr.png", scale=8)