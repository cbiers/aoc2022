def findMaxY(l):
    m = -1
    for x, y in l:
        m = max(m, y)
    return m

def moveSand(pos, b, s, m):
    x, y = pos
    if y + 1 == m:
        return pos
    if (x, y + 1) not in b and (x, y + 1) not in s:
        return [x, y + 1]
    if (x - 1, y + 1) not in b and (x - 1, y + 1) not in s:
        return [x - 1, y + 1]
    if (x + 1, y + 1) not in b and (x + 1, y + 1) not in s:
        return [x + 1, y + 1]
    return pos

f = open("input.txt", "r")
lines = f.readlines()

blocked = []
sand = []

for line in lines:
    coords = []
    parts = line.split(" -> ")
    for part in parts:
        coords.append([int(i) for i in part.split(",")])
    for i in range(len(coords) - 1):
        if coords[i][0] == coords[i + 1][0]:
            for j in range(min(coords[i][1], coords[i + 1][1]), max(coords[i][1], coords[i + 1][1]) + 1):
                if (coords[i][0], j) not in blocked:
                    blocked.append((coords[i][0], j))
        else:
            for j in range(min(coords[i][0], coords[i + 1][0]), max(coords[i][0], coords[i + 1][0]) + 1):
                if (j, coords[i][1]) not in blocked:
                    blocked.append((j, coords[i][1]))

maxY = findMaxY(blocked) + 2

overflow = False
resting = False
sandPos = [500, 0]
count = 0

while (500, 0) not in sand:
    oldPos = sandPos
    sandPos = moveSand(sandPos, blocked, sand, maxY)
    if sandPos == oldPos:
        sand.append((sandPos[0], sandPos[1]))
        sandPos = [500,0]
        count += 1

print count
