cycleThresholds = { 20, 60, 100, 140, 180, 220 }
x, cycle = 1, 0
signalStrengths = []

for line in open("Day10-input.txt", "r"):
    line = line.strip().split(" ")
    cycle += 1
    if cycle in cycleThresholds:
        signalStrengths.append(x * cycle)
    if len(line) == 1: continue
    cycle += 1
    if cycle in cycleThresholds:
        signalStrengths.append(x * cycle)
    x += int(line[1])

print(sum(signalStrengths))