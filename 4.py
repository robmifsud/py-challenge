import requests
import urllib
import re

# Start
# nothing = '12345' 

# Checkpoint 1 - divide 16044 by two and keep going
nothing = '8022'

for i in range(400):
    r = requests.get(f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={nothing}')
    print(r.content)
    match = re.findall('(?<=and the next nothing is )\d+', str(r.content))
    nothing = match[0]

# ans: peak.html
