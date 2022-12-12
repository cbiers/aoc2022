f = open("input.txt", "r")
lines = f.readlines()

def getNeighbors(n, v, xL, yL, m):
    res = []
    x, y = n
    if x > 0:
        if (x-1, y) not in v and m[(x-1, y)] <= m[n] + 1:
            res.append((x-1, y))
    if y > 0:
        if (x, y-1) not in v and m[(x, y-1)] <= m[n] + 1:
            res.append((x, y-1))
    if x < xL:
        if (x+1, y) not in v and m[(x+1, y)] <= m[n] + 1:
            res.append((x+1, y))
    if y < yL:
        if (x, y+1) not in v and m[(x, y+1)] <= m[n] + 1:
            res.append((x, y+1))
    return res


INF = 1000000

map = {}
starts = []
end = ()

countY = 0

for line in lines:
    countX = 0
    for char in line[:-1]:
        if char == "S":
            toAdd = ord("a")
            starts.append((countX, countY))
        elif char == "E":
            end = (countX, countY)
            toAdd = ord("z")
        else:
            toAdd = ord(char)
            if char == "a":
                starts.append((countX, countY))
        map[(countX, countY)] = toAdd
        countX += 1
    countY += 1

xLen = len(lines[0]) - 2
yLen = len(lines) - 1

res = []

for start in starts:

    visited = []
    distances = {}

    for key in map.keys():
        distances[key] = INF
    distances[start] = 0

    current = start
    fringe = []

    while end not in visited:
        visited.append(current)
        ext = getNeighbors(current, visited, xLen, yLen, map)
        for e in ext:
            if e not in fringe:
                fringe.append(e)
        newDist = distances[current] + 1
        for n in fringe:
            if distances[n] > newDist:
                distances[n] = newDist
        if len(fringe) == 0:
            break
        current = fringe[0]
        fringe.remove(current)

    if end in visited:
        res.append(distances[end])

print min(res)
