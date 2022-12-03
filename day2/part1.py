file = open('file.txt', 'r')
ties = {
   'X' : 'A',
   'Y' : 'B',
   'Z' : 'C' 
}
wins = {
    'X' : 'C',
    'Y' : 'A',
    'Z' : 'B'
}
scores = {'X' : 1,
          'Y' : 2,
          'Z' : 3
}
score = 0
tie = 3
win = 6
for line in file:
    p1 = line[2]
    p2 = line[0]
    score += scores[p1]
    if wins[p1] == p2:
        score += win
        continue
    if ties[p1] == p2:
        score +=tie
print(score)