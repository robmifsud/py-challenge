import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('huge', 'file')
r = requests.get('http://www.pythonchallenge.com/pc/return/evil4.jpg', auth=auth)
# Returns: Bert is evil, go back

data = open('./evil2.gfx', 'rb').read()
for i in range(5):
    open(f'{i}.jpg', 'wb').write(data[i::5])

# ans: 5 images spelling out disproportional
