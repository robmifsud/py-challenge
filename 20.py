from PIL import Image, ImageEnhance
from requests.auth import HTTPBasicAuth
import requests
import base64


data = open('./unreal.jpg', 'rb')
im = Image.open('./unreal.jpg', 'r')
# print(data.read())

# im = im.convert('1')
# fil = ImageEnhance.Contrast(im)
# im = fil.enhance(1.25)
# im = im.transpose(Image.Transpose.ROTATE_180)
im = im.crop((57, 0, 290, 75))
red, green, blue = im.split()
# red.show()
# green.show()
# blue.show()

w, h = im.size

# im.transpose(Image.Transpose.ROTATE_180)
# im.show()

# for i in range(h):
#     for j in range(w):
#         print(im.getpixel((j, i)))
#         if im.getpixel((j, i)) == (167, 195, 206):
#             im.putpixel((j, i), (0, 0, 0))

# im.show()

# hint : try requesting image and using base64?
auth = HTTPBasicAuth('butter', 'fly')
headers = {'Range' : 'bytes=30202-60404'}
r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth=auth, headers=headers)
print(f'Respoinse: {r}, Headers: {r.headers}, Content: {r.content}')
data = base64.b64decode(r.content)
# print(data)
