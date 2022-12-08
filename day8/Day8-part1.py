trees = {}

f = open("Day8-input.txt", "r")
i = 0
for line in f:
    line = line.strip()
    j = 0
    for t in line:
        trees[i, j] = int(t)
        j += 1
    i += 1

lineLength = i
visibleTrees = []

for c, h in trees.items():
    if c[0] == 0 or c[1] == 0 or c[0] == lineLength-1 or c[1] == lineLength-1:
        visibleTrees.append(trees[c])
        continue
    x = c[1]
    y = c[0]
    currentTreeHeight = trees[c]
    visible = True
    for i in range(x-1, -1, -1):
        if trees[y, i] >= currentTreeHeight:
            visible = False
            break
    if visible:
        visibleTrees.append(trees[c])
    else:
        visible = True
        for i in range(x+1, lineLength):
            if trees[y, i] >= currentTreeHeight:
                visible = False
                break
        if visible:
            visibleTrees.append(trees[c])
        else:
            visible = True
            for i in range(y-1, -1, -1):
                if trees[i, x] >= currentTreeHeight:
                    visible = False
                    break
            if visible:
                visibleTrees.append(trees[c])
            else:
                visible = True
                for i in range(y+1, lineLength):
                    if trees[i, x] >= currentTreeHeight:
                        visible = False
                        break
                if visible:
                    visibleTrees.append(trees[c])

print(len(visibleTrees))