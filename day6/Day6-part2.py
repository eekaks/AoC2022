howManyChecked = 0
checkList = []
characters = []

for line in open("Day6-input.txt", "r"):
    for c in line:
        characters.append(c)

for c in characters:
    if howManyChecked >= 14 :
        if len(set(checkList)) >= 14:
            break
        checkList.remove(characters[howManyChecked-14])
    checkList.append(c)
    howManyChecked += 1

print(howManyChecked)