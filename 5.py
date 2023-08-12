import requests
import pickle

with open('banner.p', 'rb') as f:
    data = pickle.load(f)
    for line in data:
        for tup in line:
            for i in range(tup[1]):
                print(tup[0], end='')
        print()

# Hash art in terminal, ans: channel
