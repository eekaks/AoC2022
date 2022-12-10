cycleThresholds = { 39, 79, 119, 159, 199, 239 }
x = 1
position = -1
image = []

f = open("Day10-input.txt", "r")
for line in f:
    line = line.strip().split(" ")
    position += 1
    if abs(x - position) <= 1:
        image.append('#')
    else:
        image.append('.')
    if position >= 39:
            position = -1
    if len(line) == 1:
        continue
    position += 1
    if abs(x - position) <= 1:
        image.append('#')
    else:
        image.append('.')
    if position >= 39:
        position = -1
    x += int(line[1])
    
 
for i in range(len(image)):
    print(image[i], end='')
    if i in cycleThresholds:
        print()
