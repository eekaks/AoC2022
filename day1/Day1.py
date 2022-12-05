elf_calories = []
one_elf_calories = 0
f = open("Day1-input.txt", "r")
for calorie_line in f:
    if calorie_line.strip() == "":
        elf_calories.append(one_elf_calories)
        one_elf_calories = 0
        continue
    one_elf_calories += int(calorie_line.strip())
elf_calories.append(one_elf_calories)

elf_calories.sort(reverse = True)
print(elf_calories)
answer = 0
for i in range(3):
    answer += elf_calories[i]
print(answer)