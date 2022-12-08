f = open("input.txt", "r")
lines = f.readlines()

forest = []

for line in lines:
    forest.append([int(i) for i in line[:-1]])

c = len(forest[0])
l = len(forest)

best = 0

for i in range(1, l - 1):
    for j in range(1, c - 1):
        viewN = 0
        viewE = 0
        viewS = 0
        viewW = 0
        for k in range(i - 1, -1, -1):
            if forest[k][j] >= forest[i][j] or k == 0:
                viewN = i - k
                break
        for k in range(i + 1, l):
            if forest[k][j] >= forest[i][j] or k == l - 1:
                viewS = k - i
                break
        for k in range(j - 1, -1, -1):
            if forest[i][k] >= forest[i][j] or k == 0:
                viewW = j - k
                break
        for k in range(j + 1, c):
            if forest[i][k] >= forest[i][j] or k == c - 1:
                viewE = k - j
                break
        view = viewN * viewS * viewW * viewE
        if view > best:
            best = view

print best
