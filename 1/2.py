f = open("input.txt", "r")
lines = f.readlines()

sm = 0
sums = []
for line in lines:
    if not line[:-1]:
        sums.append(sm)
        sm = 0
    else:
        sm += int(line[:-1])

maxs = []
for i in range(0, 3):
    mx = max(sums)
    sums.remove(mx)
    maxs.append(mx)

print sum(maxs)
