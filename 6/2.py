f = open("input.txt", "r")
line = f.readlines()[0][:-1]

chars = [line[i] for i in range(14)]

res = -1

for i in range(14, len(line)):
    if len(set(chars)) == 14:
        res = i
        break
    chars.append(line[i])
    chars.pop(0)

print res
