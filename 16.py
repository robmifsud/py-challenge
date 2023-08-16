from PIL import Image

im = Image.open('./mozart.gif', 'r')
pal = im.getpalette()
w, h = im.size

# Exactly 5 '195' colored pixels in each row:
# for j in range(h):
#     c = 0
#     for i in range(w):
#         pix = im.getpixel((i, j))
#         if pix == 195:
#             c += 1
#     print(f'Row: {j} Count: {c}')

new = Image.new('P', (1920, 480))
new.putpalette(pal) # copy pallete to retain colors
first = im.crop((0, 0, 640, 1))
new.paste(first, (640, 0))

# get baseline where purple pixels will be (constant according to first row)
base = 0
for i in range(1920):
    if new.getpixel((i, 0)) == 195:
        base = i
        break

for i in range(1, h):
    for j in range(w):
        if im.getpixel((j, i)) == 195:
            # rows.append((im.crop((0, i, 640, i+1)), j))
            # subtract distance from baseline and paste to new
            new.paste((im.crop((0, i, w, i+1))), (base-j, i))
            break

new.show() # ans: romance
