f = open("input.txt", "r")
lines = f.readlines()

sum = 0
sums = []
for line in lines:
    if not line[:-1]:
        sums.append(sum)
        sum = 0
    else:
        sum += int(line[:-1])

print max(sums)
