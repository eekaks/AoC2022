overlappingPairs = 0

class Assignment:
    def __init__(self, range):
        self.start = int(range.split("-")[0])
        self.end = int(range.split("-")[1])

for line in open("Day4-input.txt", "r"):
    line = line.strip().split(",")
    first_elf = Assignment(line[0])
    second_elf = Assignment(line[1])
    
    if first_elf.start <= second_elf.end and second_elf.start <= first_elf.end:
        overlappingPairs += 1

print(overlappingPairs)