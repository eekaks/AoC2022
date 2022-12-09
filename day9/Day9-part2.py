tailVisited = {(0, 0)}
knots = [(0,0) for i in range(10)]
directions = {"R" : (1, 0), "L" : (-1, 0), "U" : (0, 1), "D" : (0, -1)}

f = open("Day9-input.txt", "r")
for line in f:
    for i in range(int(line[2:])):
        for j in range(9):
            knot = knots[j]
            nextKnot = knots[j+1]
            if j == 0:
                knot = (knot[0] + directions[line[0]][0], knot[1] + directions[line[0]][1])
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
            
        tailVisited.add(knots[9])
        
print(len(tailVisited))