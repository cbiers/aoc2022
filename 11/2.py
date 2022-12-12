import math

class Monkey:
    def __init__(self, items, operator, operand, test, true, false):
        self.items = items
        self.operator = operator
        self.operand = operand
        self.test = test
        self.true = true
        self.false = false
        self.count = 0

    def worryLevels(self):
        self.count += len(self.items)
        for i in range(len(self.items)):
            if self.operator == "*":
                self.items[i] *= self.operand
            elif self. operator == "+":
                self.items[i] += self.operand
            else:
                self.items[i] *= self.items[i]
            self.items[i] = self.items[i] % 9699690

    def testItem(self, item):
        return item % self.test == 0

    def __str__(self):
        s = "Monkey with items " + str(self.items) + "\n"
        s += "Operation: " + self.operator + ", operand: " + str(self.operand) + "\n"
        s += "Test: divisible by " + str(self.test) + "\n"
        s += "if true: monkey " + str(self.true) + ", if false: monkey " + str(self.false) + "\n"
        s += "Monkey counted " + str(self.count) + " items" + "\n"
        s += "----------------"
        return s

monkeys = [Monkey([54, 98, 50, 94, 69, 62, 53, 85], "*", 13, 3, 2, 1), Monkey([71, 55, 82], "+", 2, 13, 7, 2), Monkey([77, 73, 86, 72, 87], "+", 8, 19, 4, 7), Monkey([97, 91], "+", 1, 17, 6, 5), Monkey([78, 97, 51, 85, 66, 63, 62], "*", 17, 5, 6, 3), Monkey([88], "+", 3, 7, 1, 0), Monkey([87, 57, 63, 86, 87, 53], "square", None, 11, 5, 0), Monkey([73, 59, 82, 65], "+", 6, 2, 4, 3)]

for i in range(10000):
    print i
    for monkey in monkeys:
        monkey.worryLevels()
        for item in monkey.items:
            if monkey.testItem(item):
                monkeys[monkey.true].items.append(item)
            else:
                monkeys[monkey.false].items.append(item)
        monkey.items = []

counts = [monkey.count for monkey in monkeys]
counts.sort()
print counts[-1] * counts[-2]
