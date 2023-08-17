from PIL import Image, ImageEnhance
import zipfile
import gzip
import difflib


im = Image.open('./balloons.jpg', 'r')

im_l = im.crop((0, 0, 375, 335))
im_r = im.crop((375, 0, 750, 335))

data = gzip.open('./deltas.gz')

l1, l2 = [], []
for line in data:
    l1.append(line.decode()[:53]+'\n')
    l2.append(line.decode()[56:])

com = difflib.Differ().compare(l1, l2)

f = open("18_f.png", "wb")
f1 = open("18_f1.png", "wb")
f2 = open("18_f2.png", "wb")

for line in com:
    bs = bytes([int(o, 16) for o in line[2:].strip().split(" ") if o])
    if line[0] == '+':
        f1.write(bs)
    elif line[0] == '-':
        f2.write(bs)
    else:
        f.write(bs)

f.close()
f1.close()
f2.close()
