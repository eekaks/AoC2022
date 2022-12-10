cycleThresholds = { 20, 60, 100, 140, 180, 220 }
x = 1
cycle = 0
signalStrengths = []

f = open("Day10-input.txt", "r")
for line in f:
    line = line.strip().split(" ")
    cycle += 1
    if cycle in cycleThresholds:
        print(f"cycle: {cycle} x: {x}")
        signalStrengths.append(x * cycle)
    if len(line) == 1:
        continue
    cycle += 1
    if cycle in cycleThresholds:
        print(f"cycle: {cycle} x: {x}")
        signalStrengths.append(x * cycle)
    x += int(line[1])
 
print(signalStrengths)
print(sum(signalStrengths))