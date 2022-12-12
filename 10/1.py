f = open("input.txt", "r")
lines = f.readlines()

cycles = [1]

for line in lines:
    parts = line[:-1].split()
    cycles.append(cycles[-1])
    if parts[0] == "addx":
        cycles.append(cycles[-1] + int(parts[1]))

sum = 0
for i in range (19, 220, 40):
    sum += cycles[i] * (i + 1)
print sum
