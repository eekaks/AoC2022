directorySizes = { "root/" : 0 }
directoryPath = "root/"

for line in open("Day7-input.txt", "r"):
    lineParts = line.strip().split(" ")

    if lineParts[0] == "$":
        if lineParts[1] == "cd":
            if lineParts[2] == "..":
                marker = directoryPath[:-1].rfind("/")
                directoryPath = directoryPath[:marker+1]
            elif lineParts[2] == "/":
                continue
            else:
                directoryPath += lineParts[2] + "/"          

    else:
        if directoryPath not in directorySizes:
                directorySizes[directoryPath] = 0
        if lineParts[0] != "dir":
            for path in directorySizes:
                if directoryPath.find(path) != -1:
                    directorySizes[path] += int(lineParts[0])

spaceNeeded = 30000000-(70000000-directorySizes["root/"])

totalSizeOfDirToDelete = 70000000
for k, v in directorySizes.items():
    if v >= spaceNeeded:
        if v < totalSizeOfDirToDelete:
            totalSizeOfDirToDelete = v
    
print(totalSizeOfDirToDelete)