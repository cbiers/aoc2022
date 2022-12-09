def updateTail(h, t):
    deltaX = h[0] - t[0]
    deltaY = h[1] - t[1]
    if deltaX > 1:
        t[0] += 1
        t[1] = h[1]
    elif deltaX < -1:
        t[0] -= 1
        t[1] = h[1]
    if deltaY > 1:
        t[1] += 1
        t[0] = h[0]
    elif deltaY < -1:
        t[1] -= 1
        t[0] = h[0]

f = open("input.txt", "r")
lines = f.readlines()

headPos = [0, 0]
tailPos = [0, 0]
visited = [(0, 0)]

for line in lines:
    move = line[:-1].split()
    dir = move[0]
    dist = int(move[1])
    for i in range(dist):
        if dir == "U":
            headPos[1] += 1
        elif dir == "D":
            headPos[1] -= 1
        elif dir == "L":
            headPos[0] -= 1
        else:
            headPos[0] += 1
        updateTail(headPos, tailPos)
        visited.append(tuple(tailPos))

print len(set(visited))
