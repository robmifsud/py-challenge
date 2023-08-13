from PIL import Image

im = Image.open('./cave.jpg', 'r')

w, h = im.size

change = True

for i in range(w):
    if (i == 0) or (i % 2 == 0):
        change = True
    else:
        change = False
    for j in range(h):
        change = not change
        if change:
            im.putpixel((i, j), (0, 0, 0))

im.show() # ans: evil
