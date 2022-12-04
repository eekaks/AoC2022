import string
import time

t1 = time.perf_counter()


letters = string.ascii_lowercase + string.ascii_uppercase

letter_priorities = {}

for i in range(1, 53):
    letter_priorities[letters[i-1]] = i

priority_sum = 0

f = open("Day3-input.txt", "r")

inputs = []
for line in f:
    inputs.append(line.strip())

for i in range(0, len(inputs), 3):
    elf_group = inputs[i: i+3]
    elf_group_first_sack = set()
    elf_group_second_sack = set()
    
    for item in elf_group[0]:
        elf_group_first_sack.add(item)
    
    for item in elf_group[1]:
        elf_group_second_sack.add(item)

    for item in elf_group[2]:
        if item in elf_group_first_sack and item in elf_group_second_sack:
            priority_sum += letter_priorities[item]   
            break  

print(priority_sum)

t2 = time.perf_counter()
print(f"Execution time: {t2 - t1:0.6f} seconds")