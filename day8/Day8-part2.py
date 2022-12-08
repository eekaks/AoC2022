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
highestScenicScore = 0

for c, h in trees.items():
    if c[0] == 0 or c[1] == 0 or c[0] == lineLength-1 or c[1] == lineLength-1:
        continue
    x = c[1]
    y = c[0]
    currentTreeHeight = trees[c]
 
    viewLeft = 1
    for i in range(x-1, -1, -1):
        if trees[y, i] >= currentTreeHeight:
            break
        if i != 0:
            viewLeft += 1
    
    viewRight = 1
    for i in range(x+1, lineLength):
        if trees[y, i] >= currentTreeHeight:
            break
        if i != lineLength-1:
            viewRight += 1
       
    viewUp = 1
    for i in range(y-1, -1, -1):
        if trees[i, x] >= currentTreeHeight:
            break
        if i != 0:
            viewUp += 1
            
    viewDown = 1        
    for i in range(y+1, lineLength):
        if trees[i, x] >= currentTreeHeight:
            break
        if i != lineLength-1:
            viewDown += 1
    
    scenicScore = viewLeft*viewRight*viewUp*viewDown
    if scenicScore >= highestScenicScore:
        highestScenicScore = scenicScore
                
print(highestScenicScore)