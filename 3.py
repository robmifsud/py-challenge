import re


with open('3.txt', 'r') as f:
    s = f.read()
    # Need to use negative lookbehind/lookahead to ensure exactly 3 uppercase letters
    matches = re.findall('(?<![A-Z])[A-Z]{3}[a-z][A-Z]{3}(?![A-Z])', s)
    for m in matches:
        print(m[3], end='')

# ans: linkedlist
