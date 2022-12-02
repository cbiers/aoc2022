f = open("input.txt", "r")
lines = f.readlines()

rock = ["A", "X"]
paper = ["B", "Y"]
scissors = ["C", "Z"]
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
        if two in rock:
            score += draw + r
        elif two in paper:
            score += win + p
        else:
            score += s
    elif one in paper:
        if two in paper:
            score += draw + p
        elif two in scissors:
            score += win + s
        else:
            score += r
    else:
        if two in scissors:
            score += draw + s
        elif two in rock:
            score += win + r
        else:
            score += p

print score
