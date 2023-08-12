from collections import Counter

with open('2.txt', 'r') as f:
    s = f.read()
    print(Counter(s))

# ans: equality