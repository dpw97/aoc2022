import string
file = open('file.txt','r')
d = dict.fromkeys(string.ascii_letters, 0)
i = 1

for key in d:
    d[key] = i
    i+=1

total = 0
mod3 = 1
lines = []

for line in file:
    lines.append(line.rstrip())
    print(lines)
    if mod3 % 3 == 0:
        print(lines)
        intersec = ''.join(set(lines[0]) & set(lines[1]) & set(lines[2]))
        total += d[intersec]
        lines.clear()
    mod3 += 1
print(total)