def handleWin(p1, p2):
    if p1 == 'X' and p2 == 'C':
        return True
    if p1 == 'Y' and p2 == 'A':
        return True
    if p1 == 'Z' and p2 == 'B':
        return True   
    return False
def handleTie(p1,p2):
    if p1 == 'X' and p2 == 'A':
        return True
    if p1 == 'Y' and p2 == 'B':
        return True
    if p1 == 'Z' and p2 == 'C':
        return True  
    return False

file = open('file.txt', 'r')
scores = {'X' : 1,
          'Y' : 2,
          'Z' : 3}
score = 0
tie = 3
win = 6
for line in file:
    p1 = line[2]
    p2 = line[0]
    score += scores[p1]
    if handleTie(p1,p2):
        score +=tie
        continue
    if handleWin(p1,p2): score += win

print(score)