from collections import deque 

startSituationNotRead = True
craneStacks = {}

f = open("Day5-input.txt", "r")
lines = f.readlines()
for line in lines:
    if line.strip() == "":
        startSituationNotRead = False
        continue
    elif (line.strip() != "") and line[1] == "1":
        continue
    if startSituationNotRead:
        for i in range(1, len(line), 4):
            if i not in craneStacks:
                craneStacks[i] = deque()
            if line[i] != " ":
                craneStacks[i].appendleft(line[i])
    else:
        line = line.strip().split(" ")
        howMany = int(line[1])
        fromStack = int(line[3])
        toStack = int(line[5])
        modifier = 4
        if howMany == 1:
            for i in range(howMany):
                crateToMove = craneStacks[(fromStack*modifier)-3].pop()
                craneStacks[(toStack*modifier)-3].append(crateToMove)
        else:
            temporaryQueue = deque()
            for i in range(howMany):
                crateToMove = craneStacks[(fromStack*modifier)-3].pop()
                temporaryQueue.append(crateToMove)
            for i in range(howMany):
                crateToMove = temporaryQueue.pop()
                craneStacks[(toStack*modifier)-3].append(crateToMove)
print(craneStacks)

answer = ""
for k, v in craneStacks.items():
    answer += craneStacks[k].pop()
print(answer)