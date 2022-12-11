from collections import deque

class Monkey:
    def __init__(self, items, operation, divisibleTest, trueTarget, falseTarget):
        self.items = items
        self.operation = operation
        self.divisibleTest = divisibleTest
        self.trueTarget = trueTarget
        self.falseTarget = falseTarget
        self.inspections = 0

    def inspectItem(self, reduceNumber):
        self.inspections += 1
        self.items[0] = self.doOperation(self.items[0])
        target = self.doTest(self.items[0])
        self.items[0] %= reduceNumber
        return self.items.popleft(), target

    def doOperation(self, item):
        operation = self.operation.split(" ")
        if operation[0] == "*":
            if operation[1] == "old":
                return item * item
            else:
                return item * int(operation[1])
        else:
            if operation[1] == "old":
                return item + item
            else:
                return item + int(operation[1])

    def doTest(self, item):
        if item % self.divisibleTest == 0:
            return self.trueTarget
        else:
            return self.falseTarget

monkeys = []
for line in open("Day11-input.txt"):
    line = line.strip().split(" ")
    if len(line) == 1:
        monkeys.append(Monkey(monkeyItems, operationString, testOperation, trueTarget, falseTarget))
        continue
    if line[0] == "Starting":
        monkeyItems = deque()
        for i in range(2, len(line)):
            if line[i][-1] == ",":
                line[i] = line[i][:-1]
            monkeyItems.append(int(line[i]))
    elif line[0] == "Operation:":
        operationString = f"{line[4]} {line[5]}"
    elif line[0] == "Test:":
        testOperation = int(line[3])
    elif line[1] == "true:":
        trueTarget = int(line[5])
    elif line[1] == "false:":
        falseTarget = int(line[5])
monkeys.append(Monkey(monkeyItems, operationString, testOperation, trueTarget, falseTarget))

reduceNumber = 1
for monkey in monkeys:
    reduceNumber *= monkey.divisibleTest

for i in range(10000):
    for m in monkeys:
        for i in range(len(m.items)):
            itemToThrow, targetMonkey = m.inspectItem(reduceNumber)
            monkeys[targetMonkey].items.append(itemToThrow)

monkeys.sort(key=lambda x: x.inspections, reverse=True)
print(monkeys[0].inspections * monkeys[1].inspections)