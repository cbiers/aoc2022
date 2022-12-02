f = open("input.txt", "r")
lines = f.readlines()

rock = ["A"]
paper = ["B"]
scissors = ["C"]
w = ["Z"]
d = ["Y"]
win = 6
draw = 3
r = 1
p = 2
s = 3

score = 0

for line in lines:
    play = line.split()
    one, two = play[0], play[1]
    if one in rock:
        if two in w:
            score += win + p
        elif two in d:
            score += draw + r
        else:
            score += s
    elif one in paper:
        if two in w:
            score += win + s
        elif two in d:
            score += draw + p
        else:
            score += r
    else:
        if two in w:
            score += win + r
        elif two in d:
            score += draw + s
        else:
            score += p

print score
