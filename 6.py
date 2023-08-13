import re
import zipfile

nothing = '90052'
archive = zipfile.ZipFile('./channel.zip', 'r')
comments = []

for i in range(910):
    # print(archive.getinfo(f'{nothing}.txt').comment)
    comments.append(archive.getinfo(f'{nothing}.txt').comment.decode('utf-8'))
    with open(f'./channel/{nothing}.txt', 'r') as f:
        content = f.read()
        # print(content)
        r = re.findall('(?<=Next nothing is )\d+', content)
        if r:
            nothing = r[0]
        else:
            break

for c in comments:
    print(c, end='')

# ans: oxygen (hidden in the bigger word hockey)
