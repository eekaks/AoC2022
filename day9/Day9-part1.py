tailVisited = { (0, 0) : 1 }
head, tail = (0, 0), (0, 0)
xDirection = 1
yDirection = 1

f = open("Day9-input.txt", "r")
for line in f:
    line = line.strip()
    if line[0] == "R":
        xDirection = 1
        yDirection = 0
    elif line[0] == "L":
        xDirection = -1
        yDirection = 0
    elif line[0] == "U":
        xDirection = 0
        yDirection = 1
    elif line[0] == "D":
        xDirection = 0
        yDirection = -1

    for i in range(int(line[2:])):
        if tail in tailVisited:
            tailVisited[tail] += 1
        else:
            tailVisited[tail] = 1
        print()
        print(f"Head: {head}")
        print(f"Tail: {tail}")
        head = (head[0] + xDirection, head[1] + yDirection)
        if abs(head[0] - tail[0]) <= 1 and abs(head[1] - tail[1]) <= 1:
            continue
        if head[0] - tail[0] > 1:
            if head[1] == tail[1]:
                tail = (tail[0] + 1, tail[1])
            else:
                if head[1] > tail[1]:
                    tail = (tail[0] + 1, tail[1] + 1)
                else:
                    tail = (tail[0] + 1, tail[1] - 1)
        
        elif head[0] - tail[0] < -1:
            if head[1] == tail[1]:
                tail = (tail[0] - 1, tail[1])
            else:
                if head[1] > tail[1]:
                    tail = (tail[0] - 1, tail[1] + 1)
                else:
                    tail = (tail[0] - 1, tail[1] - 1)

        elif head[1] - tail[1] > 1:
            if head[0] == tail[0]:
                tail = (tail[0], tail[1] + 1)
            else:
                if head[0] > tail[0]:
                    tail = (tail[0] + 1, tail[1] + 1)
                else:
                    tail = (tail[0] - 1, tail[1] + 1)
        
        elif head[1] - tail[1] < -1:
            if head[0] == tail[0]:
                tail = (tail[0], tail[1] - 1)
            else:
                if head[0] > tail[0]:
                    tail = (tail[0] + 1, tail[1] - 1)
                else:
                    tail = (tail[0] - 1, tail[1] - 1)

print(tailVisited)
print(len(tailVisited))