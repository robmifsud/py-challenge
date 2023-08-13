a = ['1', '11', '21', '1211', '111221']
# look and say sequence

for i in range(4, 31):
    term = a[i]
    next = ''
    count = 1

    for j in range(1, len(term)):
        if term[j] == term[j-1]:
            count += 1
        else:
            next += f'{count}{term[j-1]}'
            count = 1
    next += f'{count}{term[-1]}'
    a.append(next)

print(len(a[30])) # ans: 5808
