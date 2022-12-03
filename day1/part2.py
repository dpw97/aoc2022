f = open('file.txt', 'r')

mnums = [] 

cm = 0

for line in f:
    if line == '\n':
        mnums.append(cm)
        cm = 0
    else:
        cm +=int(line)
mnums.sort()
print(mnums[-1] + mnums[-2] + mnums[-3])