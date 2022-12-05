f = open("input.txt", "r")
lines = f.readlines()

count = 0

for line in lines:
    pairs = line[:-1].split(",")
    pair1 = pairs[0].split("-")
    pair2 = pairs[1].split("-")
    if (int(pair1[0]) <= int(pair2[0]) and int(pair1[1]) >= int(pair2[1])) or (int(pair2[0]) <= int(pair1[0]) and int(pair2[1]) >= int(pair1[1])):
        count += 1

print count
