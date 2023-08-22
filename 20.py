from requests.auth import HTTPBasicAuth
import requests
import re


# hint : try requesting image and using base64?
auth = HTTPBasicAuth('butter', 'fly')

r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth=auth)
range = r.headers.get('Content-Range')
start = re.findall('(?<=-)\d+', range)[0]
while True:
    headers = {'Range' : f'bytes={int(start)+1}-'}
    req = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth=auth, headers=headers)
    if len(req.content) != 0:
        print(req.headers)
        range = req.headers.get('Content-Range')
        start = re.findall('(?<=-)\d+', range)[0]
    else:
        break

headers = {'Range' : 'bytes=1152983631-'}
r = requests.get('http://www.pythonchallenge.com/pc/hex/unreal.jpg', auth=auth, headers=headers)
print(f'Respoinse: {r}, Headers: {r.headers}, Content: {r.content}')

# invader in reverse: redavni
# and it is hiding at 1152983631
file = open('./20.zip', 'wb')
file.write(r.content)
