f = open("input.txt", "r")
lines = f.readlines()

cycles = [1]

for line in lines:
    parts = line[:-1].split()
    cycles.append(cycles[-1])
    if parts[0] == "addx":
        cycles.append(cycles[-1] + int(parts[1]))

curr = 0
s = ""
for cycle in cycles:
    if curr in ([cycle-1, cycle, cycle+1]):
        s += "#"
    else:
        s += "."
    curr += 1
    if curr % 40 == 0:
        print s
        s = ""
        curr = 0
