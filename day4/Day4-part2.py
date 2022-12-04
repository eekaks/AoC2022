overlappingPairs = 0

class Assignment:
    def __init__(self, range):
        self.start = int(range.split("-")[0])
        self.end = int(range.split("-")[1])

f = open("Day4-input.txt", "r")
for line in f:
    line = line.strip().split(",")
    first_elf = Assignment(line[0])
    second_elf = Assignment(line[1])
    
    if (first_elf.start >= second_elf.start and first_elf.end <= second_elf.end) or (second_elf.start >= first_elf.start and second_elf.end <= first_elf.end):
        overlappingPairs += 1
        print(f"{first_elf.start}-{first_elf.end}")
        print(f"{second_elf.start}-{second_elf.end}")

print(overlappingPairs)