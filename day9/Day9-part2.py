tailVisited = { (0, 0) : 1 }
knots = [(0,0) for i in range(10)]
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
        if knots[9] in tailVisited:
            tailVisited[knots[9]] += 1
        else:
            tailVisited[knots[9]] = 1
        for j in range(9):
            knot = knots[j]
            nextKnot = knots[j+1]
            if j == 0:
                knot = (knot[0] + xDirection, knot[1] + yDirection)
            if abs(knot[0] - nextKnot[0]) <= 1 and abs(knot[1] - nextKnot[1]) <= 1:
                knots[j] = knot
                knots[j+1] = nextKnot
                continue
            if knot[0] - nextKnot[0] > 1:
                if knot[1] == nextKnot[1]:
                    nextKnot = (nextKnot[0] + 1, nextKnot[1])
                else:
                    if knot[1] > nextKnot[1]:
                        nextKnot = (nextKnot[0] + 1, nextKnot[1] + 1)
                    else:
                        nextKnot = (nextKnot[0] + 1, nextKnot[1] - 1)
            
            elif knot[0] - nextKnot[0] < -1:
                if knot[1] == nextKnot[1]:
                    nextKnot = (nextKnot[0] - 1, nextKnot[1])
                else:
                    if knot[1] > nextKnot[1]:
                        nextKnot = (nextKnot[0] - 1, nextKnot[1] + 1)
                    else:
                        nextKnot = (nextKnot[0] - 1, nextKnot[1] - 1)

            elif knot[1] - nextKnot[1] > 1:
                if knot[0] == nextKnot[0]:
                    nextKnot = (nextKnot[0], nextKnot[1] + 1)
                else:
                    if knot[0] > nextKnot[0]:
                        nextKnot = (nextKnot[0] + 1, nextKnot[1] + 1)
                    else:
                        nextKnot = (nextKnot[0] - 1, nextKnot[1] + 1)
            
            elif knot[1] - nextKnot[1] < -1:
                if knot[0] == nextKnot[0]:
                    nextKnot = (nextKnot[0], nextKnot[1] - 1)
                else:
                    if knot[0] > nextKnot[0]:
                        nextKnot = (nextKnot[0] + 1, nextKnot[1] - 1)
                    else:
                        nextKnot = (nextKnot[0] - 1, nextKnot[1] - 1)
            knots[j] = knot
            knots[j+1] = nextKnot

print(len(tailVisited) + 1)