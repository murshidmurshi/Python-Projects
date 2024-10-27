import qrcode

#data to encode
data=input('enter the data:')
version=int(input('enter the version:'))  #complexiy=15
box_size=int(input('enter the box_size:'))  #max=10

qr=qrcode.QRCode(version,box_size,border=5)

qr.add_data(data)
qr.make(fit=True)

img=qr.make_image(fill='black',back='white')

f=input('enter image name as:')  #img name
img.save(f'{f}.png')

print('qrcode generated and save to the gallery')