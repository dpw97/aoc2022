file = open('file.txt', 'r')
loses = {
    'A' : 3,
    'B' : 1,
    'C' : 2
}
scores = {
    'A' : 1,
    'B' : 2,
    'C' : 3
}
wins = {
    'A' : 2,
    'B' : 3,
    'C' : 1
}
score = 0
tie = 3
win = 6
for line in file:
    result = line[2]
    shape = line[0]
    #draw
    if result == 'Y':
        score += tie
        score += scores[shape]
    #lose
    if result == 'X':
        score += loses[shape]
    #win
    if result == 'Z':
        score += wins[shape]
        score += win

print (score)