import json

def inOrder(l1, l2):
    if type(l1) == type(l2):
        if type(l1) == int:
            if l2 < l1:
                return -1
            elif l2 == l1:
                return 0
            return 1
        else:
            cont = 0
            i = 0
            while cont == 0 and i < min(len(l2), len(l1)):
                cont = inOrder(l1[i], l2[i])
                i += 1
            if cont == 0:
                if len(l2) < len(l1):
                    return -1
                elif len(l2) == len(l1):
                    return 0
                return 1
            else:
                return cont
    else:
        if type(l1) == int:
            return inOrder([l1], l2)
        else:
            return inOrder(l1, [l2])



f = open("example.txt", "r")
lines = f.readlines()

pairs = []

i = 0
while i < len(lines):
    pairs.append([json.loads(lines[i][:-1]), json.loads(lines[i+1][:-1])])
    i += 3

j = 0
sum = 0

while j < len(pairs):
    if inOrder(pairs[j][0], pairs[j][1]) == 1:
        sum += j + 1
    j += 1

print sum
