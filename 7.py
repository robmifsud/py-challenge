from PIL import Image

im = Image.open('./oxygen.png', 'r')
w, h = im.size

print(f'Width: {w}, Height: {h}')

im_crop = im.crop((0, 45, 629, 50))

print('s', end='') # First block is shorter
for i in range(5, 607, 7): # Almost all blocks are 7 pixels wide
    r, g, b, a = im_crop.getpixel((i, 0))
    print(chr(r), end='')

# ans: smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]

next = [105, 110, 116, 101, 103, 114, 105, 116, 121]

print()
for c in next:
    print(chr(c), end='') # integrity
