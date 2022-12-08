f = open("input.txt", "r")
lines = f.readlines()

forest = []

for line in lines:
    forest.append([int(i) for i in line[:-1]])

c = len(forest[0])
l = len(forest)
count = 2 * (c + l) - 4

for i in range(1, l - 1):
    for j in range(1, c - 1):
        visibleN = True
        visibleE = True
        visibleW = True
        visibleS = True
        for k in range(0, i):
            if forest[k][j] >= forest[i][j]:
                visibleN = False
        for k in range(i + 1, l):
            if forest[k][j] >= forest[i][j]:
                visibleS = False
        for k in range(0, j):
            if forest[i][k] >= forest[i][j]:
                visibleW = False
        for k in range(j + 1, c):
            if forest[i][k] >= forest[i][j]:
                visibleE = False
        if visibleN or visibleE or visibleW or visibleS:
            count += 1

print count
