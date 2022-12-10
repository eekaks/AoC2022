tailVisited = {(0, 0)}
head, tail = (0, 0), (0, 0)
directions = {"R" : (1, 0), "L" : (-1, 0), "U" : (0, 1), "D" : (0, -1)}

f = open("Day9-input.txt", "r")
for line in f:
    for i in range(int(line[2:])):
        tailVisited.add(tail)
        head = (head[0] + directions[line[0]][0], head[1] + directions[line[0]][1])

        if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
            continue

        if head[0] - tail[0] > 1:
            if head[1] == tail[1]:
                tail = (tail[0] + 1, tail[1])
            elif head[1] > tail[1]:
                tail = (tail[0] + 1, tail[1] + 1)
            else:
                tail = (tail[0] + 1, tail[1] - 1)
        
        elif head[0] - tail[0] < -1:
            if head[1] == tail[1]:
                tail = (tail[0] - 1, tail[1])
            elif head[1] > tail[1]:
                tail = (tail[0] - 1, tail[1] + 1)
            else:
                tail = (tail[0] - 1, tail[1] - 1)

        elif head[1] - tail[1] > 1:
            if head[0] == tail[0]:
                tail = (tail[0], tail[1] + 1)
            elif head[0] > tail[0]:
                tail = (tail[0] + 1, tail[1] + 1)
            else:
                tail = (tail[0] - 1, tail[1] + 1)
        
        elif head[1] - tail[1] < -1:
            if head[0] == tail[0]:
                tail = (tail[0], tail[1] - 1)
            elif head[0] > tail[0]:
                tail = (tail[0] + 1, tail[1] - 1)
            else:
                tail = (tail[0] - 1, tail[1] - 1)

print(len(tailVisited))