f = open("input.txt", "r")
lines = f.readlines()

class File:

    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return self.name + " (" + str(self.size) + ")"

class Directory:

    def __init__(self, name):
        self.name = name
        self.files = []
        self.dirs = []
        self.parent = None

    def addFile(self, file):
        self.files.append(file)

    def addDir(self, dir):
        self.dirs.append(dir)
        dir.parent = self

    def totalSize(self):
        total = 0
        for file in self.files:
            total += file.size
        for dir in self.dirs:
            total += dir.totalSize()
        return total

    def dirsWithMaxSize(self, size, l):
        ownSize = self.totalSize()
        if ownSize <= size:
            l.append(ownSize)
        for dir in self.dirs:
            dir.dirsWithMaxSize(size, l)

    def findDir(self, name):
        for dir in self.dirs:
            if dir.name == name:
                return dir

    def findFile(self, name):
        for file in self.files:
            if file.name == name:
                return file

    def __str__(self):
        res = self.name + "\n"
        for file in self.files:
            res += "-" + str(file) + "\n"
        for dir in self.dirs:
            res += "d" + str(dir) + "\n"
        return res


root = Directory("/")
current = root

for line in lines:
    parts = line[:-1].split()
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "/":
                current = root
            elif parts[2] == "..":
                current = current.parent
            else:
                current = current.findDir(parts[2])
    else:
        if parts[0] == "dir":
            if not current.findDir(parts[1]):
                current.addDir(Directory(parts[1]))
        else:
            if not current.findFile(parts[1]):
                current.addFile(File(parts[1], int(parts[0])))

l = []
root.dirsWithMaxSize(100000, l)
print sum(l)
