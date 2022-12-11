cycleThresholds = { 39, 79, 119, 159, 199, 239 }
x, position = 1, -1
image = []

for line in open("Day10-input.txt", "r"):
    line = line.strip().split(" ")
    for i in range(len(line)):
        position += 1
        image.append('#') if abs(x - position) <= 1 else image.append('.')
        if position >= 39: position = -1
    if len(line) == 2: x += int(line[1])
    
for i in range(len(image)):
    print(image[i], end='')
    if i in cycleThresholds: print()
