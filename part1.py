import math
import string
file = open('file.txt','r')
d = dict.fromkeys(string.ascii_letters, 0)
i = 1

for key in d:
    d[key] = i
    i+=1

total = 0
for line in file:
    n = math.floor(len(line) / 2)
    firstHalf = set(line[:n])
    secondHalf = set(line[n:])
    intersec = ''.join(firstHalf.intersection(secondHalf))
    total += d[intersec]
print(total)
    
