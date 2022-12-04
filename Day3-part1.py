import string

letters = string.ascii_lowercase + string.ascii_uppercase

letter_priorities = {}

for i in range(1, 53):
    letter_priorities[letters[i-1]] = i

priority_sum = 0

f = open("Day3-input.txt", "r")

for line in f:
    line = line.strip()
    line_first = line[0:len(line)//2]
    line_second = line[len(line)//2:]

    for letter in line_second:
        if letter in line_first:
            priority_sum += letter_priorities[letter]
            break

print(priority_sum)