def updateTail(p):
    for i in range(9):
        deltaX = p[i][0] - p[i+1][0]
        deltaY = p[i][1] - p[i+1][1]
        if deltaX > 1:
            p[i+1][0] += 1
            if deltaY <= 1 and deltaY >= -1:
                p[i+1][1] = p[i][1]
        elif deltaX < -1:
            p[i+1][0] -= 1
            if deltaY <= 1 and deltaY >= -1:
                p[i+1][1] = p[i][1]
        if deltaY > 1:
            p[i+1][1] += 1
            if deltaX <= 1 and deltaX >= -1:
                p[i+1][0] = p[i][0]
        elif deltaY < -1:
            p[i+1][1] -= 1
            if deltaX <= 1 and deltaX >= -1:
                p[i+1][0] = p[i][0]

f = open("input.txt", "r")
lines = f.readlines()

pos = [[0, 0] for i in range(10)]
visited = [(0, 0)]

for line in lines:
    move = line[:-1].split()
    dir = move[0]
    dist = int(move[1])
    for i in range(dist):
        if dir == "U":
            pos[0][1] += 1
        elif dir == "D":
            pos[0][1] -= 1
        elif dir == "L":
            pos[0][0] -= 1
        else:
            pos[0][0] += 1
        updateTail(pos)
        visited.append(tuple(pos[9]))

print len(set(visited))
