import requests
import re
from urllib.parse import unquote_to_bytes, quote_plus
import bz2


# Image referring to level 4?
# Get cookie data from level 4

s = requests.Session()
r = s.get('http://www.pythonchallenge.com/pc/def/linkedlist.php')
print(f'Content: {r}')
print(f'Session: {s.cookies}') # ans: you should have followed busynothing... for .pythonchallenge.com

r = s.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345')
print(f'Session: {s.cookies}')
# http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345
nothing = '12345' # start

string = ''

for i in range(400):
    r = s.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={nothing}')
    print(r.content)
    print(s.cookies.get_dict())
    string += s.cookies.get_dict()['info']
    match = re.findall('(?<=and the next busynothing is )\d+', str(r.content))
    if len(match) != 0:
        nothing = match[0]
    else:
        break

print(f'String: {unquote_to_bytes(string)}')
print(bz2.decompress(unquote_to_bytes(string)))
# is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.

# Level 13?
headers = {'Content-Type': 'application/xml'}
xml = """<?xml version='1.0' encoding='utf-8'?>
    <methodCall>
        <methodName>phone</methodName>
        <params>
            <param>
                <value><string>Leopold</string></value>
            </param>
        </params>
    </methodCall>"""
r = requests.post('http://www.pythonchallenge.com/pc/phonebook.php', data=xml, headers=headers)

print(r.content) # ans: violin

# picture of leopold http://www.pythonchallenge.com/pc/stuff/violin.php

cookies = {
    'info' : 'the flowers are on their way'
}

r = requests.post('http://www.pythonchallenge.com/pc/stuff/violin.php', cookies=cookies)

print(r)
print(r.content) # ans: balloons
