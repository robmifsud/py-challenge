from PIL import Image

im = Image.open('./wire.png', 'r')
seq = [100]
for i in range(99, 0, -1):
    seq.append(i)
    seq.append(i)

# Get image crops
crops = []
left = 0
right = 0
for s in seq:
    right += s
    crops.append(im.crop((left, 0, right, 1)))
    left = right

# Coordinate sequence
"""
0, 0
1, 0
1, 0
1, 0
1, 1
2, 1
2, 1
2, 1
2, 2
3, 2
"""

new = Image.new('RGB',(100, 100))
crop : Image

cords = []
x = 0
y = 0
c_x = 4
c_y = 1

for crop in crops:
    new.paste(crop, (x, y))
    new = new.transpose(Image.Transpose.ROTATE_90)

    if c_x != 4:
        c_x += 1
    else:
        c_x = 1
        x += 1

    if c_y != 4:
        c_y += 1
    else:
        c_y = 1
        y += 1

new = new.transpose(Image.Transpose.ROTATE_90)
new.show() # ans: image of cat. cat's name is uzi which is next level
