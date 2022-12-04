overlappingAssignments = 0

class Assignment:
    def __init__(self, range):
        self.start = int(range.split("-")[0])
        self.end = int(range.split("-")[1])

for line in open("Day4-input.txt", "r"):
    line = line.strip().split(",")
    firstElfAssignment = Assignment(line[0])
    secondElfAssignment = Assignment(line[1])
    
    if firstElfAssignment.start <= secondElfAssignment.end and secondElfAssignment.start <= firstElfAssignment.end:
        overlappingAssignments += 1

print(overlappingAssignments)