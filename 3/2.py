f = open("input.txt", "r")
lines = f.readlines()

sum = 0
i = 0

while i < len(lines):
    first = set(lines[i][:-1])
    second = set(lines[i + 1][:-1])
    third = set(lines[i + 2][:-1])
    common = list(first.intersection(second).intersection(third))[0]
    print common
    if common.islower():
        sum += ord(common) - 96
    else:
        sum += ord(common) - 38
    i += 3

print sum
