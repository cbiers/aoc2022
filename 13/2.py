f = open("input.txt", "r")
lines = f.readlines()

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



f = open("input.txt", "r")
lines = f.readlines()

pairs = []

i = 0
while i < len(lines):
    pairs.append([json.loads(lines[i][:-1]), json.loads(lines[i+1][:-1])])
    i += 3

d1 = [[2]]
d2 = [[6]]

d1pos = 1
d2pos = 2

for pair in pairs:
    if inOrder(pair[0], d1) == 1:
        d1pos += 1
    if inOrder(pair[1], d1) == 1:
        d1pos += 1
    if inOrder(pair[0], d2) == 1:
        d2pos += 1
    if inOrder(pair[1], d2) == 1:
        d2pos += 1

print d1pos * d2pos
