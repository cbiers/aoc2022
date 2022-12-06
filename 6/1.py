f = open("input.txt", "r")
line = f.readlines()[0][:-1]

chars = [line[0], line[1], line[2], line[3]]

res = -1

for i in range(4, len(line)):
    if len(set(chars)) == 4:
        res = i
        break
    chars.append(line[i])
    chars.pop(0)

print res
