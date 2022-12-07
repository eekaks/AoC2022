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

directorySizesSum = 0

for k, v in directorySizes.items():
    if v <= 100000:
        directorySizesSum += v

print(directorySizesSum)