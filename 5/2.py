f = open("input.txt", "r")
lines = f.readlines()

stacks = [
    ["P", "F", "M", "Q", "W", "G", "R", "T"],
    ["H", "F", "R"],
    ["P", "Z", "R", "V", "G", "H", "S", "D"],
    ["Q", "H", "P", "B", "F", "W", "G"],
    ["P", "S", "M", "J", "H"],
    ["M", "Z", "T", "H", "S", "R", "P", "L"],
    ["P", "T", "H", "N", "M", "L"],
    ["F", "D", "Q", "R"],
    ["D", "S", "C", "N", "L", "P", "H"]
]

for line in lines:
    s = line.split()
    n = int(s[1])
    s1 = int(s[3]) - 1
    s2 = int(s[5]) - 1
    stacks[s2].extend(stacks[s1][-n:])
    stacks[s1] = stacks[s1][:-n]

for stack in stacks:
    print stack[-1]
