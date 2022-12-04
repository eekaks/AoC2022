overlappingAssignments = 0

class Assignment:
    def __init__(self, range):
        self.start = int(range.split("-")[0])
        self.end = int(range.split("-")[1])

for line in open("Day4-input.txt", "r"):
    line = line.strip().split(",")
    firstElfAssignment = Assignment(line[0])
    secondElfAssignment = Assignment(line[1])
    
    if (firstElfAssignment.start >= secondElfAssignment.start and firstElfAssignment.end <= secondElfAssignment.end) or (secondElfAssignment.start >= firstElfAssignment.start and secondElfAssignment.end <= firstElfAssignment.end):
        overlappingAssignments += 1

print(overlappingAssignments)