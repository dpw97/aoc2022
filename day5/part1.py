from collections import deque

q = deque()
lq = [q.copy() for _ in range(10)]
FOUR = 4
with open('moves.txt', 'r') as moves:
    for line in moves:
        j = 1
        for i in range(1,34, FOUR):
            if line[i].isspace() is False:
                lq[j].appendleft(line[i])
            j+=1
with open('file.txt', 'r') as file:
    for line in file:
        nums = [int(i) for i in line.split() if i.isdigit()]
        for _ in range(nums[0]):
            lq[nums[2]].append(lq[nums[1]].pop())
            
        print(lq[nums[2]])
s = ''
for i in range(1, 10):
    s += lq[i].pop()
print(s)
