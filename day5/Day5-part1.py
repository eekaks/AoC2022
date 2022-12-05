from collections import deque 

startSituationNotRead = True
craneStacks = {}

for line in open("Day5-input-example.txt", "r"):
    print(line)
    # if len(line.strip()) == 0:
    #     startSituationNotRead = False
    if len(line.strip()) != 0 or line[1] == "1":
        startSituationNotRead = False
    if startSituationNotRead:
        for i in range(1, len(line), 4):
            if i not in craneStacks:
                craneStacks[i] = deque()
            if line[i] != " ":
                craneStacks[i].appendleft(line[i])
    elif len(line.strip()) != 0:
        line = line.split(" ")
        print(line)
        howMany = int(line[1])
        fromStack = int(line[4])
        toStack = int(line[7])
        print(howMany)
        print(fromStack)
        print(toStack)
        for i in range(howMany):
            crateToMove = craneStacks[fromStack].popright()
            craneStacks[toStack].appendright(crateToMove)

print(craneStacks)
