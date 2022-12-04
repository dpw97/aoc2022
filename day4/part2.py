with open('file.txt','r') as file:
    total = 0
    for line in file:
        l = line.split(",")
        e1 = l[0].split("-")
        e2 = l[1].rstrip('\n').split("-")

        e1Start, e1End = int(e1[0]), int(e1[1])
        e2Start, e2End = int(e2[0]), int (e2[1])

        if e1End >= e2Start and e1End <= e2End:
            total+=1
        elif e2End >= e1Start and e2End <= e1End:
            total+=1
print(total)
