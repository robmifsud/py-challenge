import requests

# r = requests.get('http://www.pythonchallenge.com/pc/phonebook.php')
# print(r.encoding)

headers = {'Content-Type': 'application/xml'}
xml = """<?xml version='1.0' encoding='utf-8'?>
    <methodCall>
        <methodName>phone</methodName>
        <params>
            <param>
                <value><string>Bert</string></value>
            </param>
        </params>
    </methodCall>"""
r = requests.post('http://www.pythonchallenge.com/pc/phonebook.php', data=xml, headers=headers)

print(r.content) # ans: italy
