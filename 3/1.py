f = open("input.txt", "r")
lines = f.readlines()

sum = 0

for line in lines:
    length = (len(line) - 1) / 2
    first = set(line[:length])
    second = set(line[length:])
    common = list(first.intersection(second))[0]
    if common.islower():
        sum += ord(common) - 96
    else:
        sum += ord(common) - 38

print sum
