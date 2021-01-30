import pyqrcode
import png

q = pyqrcode.create(input())
q.png('name.png',scale=6)
print('Qrcode generated')