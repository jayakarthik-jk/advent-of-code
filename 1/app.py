elves: list[list[str]] = []

with open("input.txt", "r", encoding="UTF-8") as file:
    elve = []
    for line in file.readlines():
        if line == "\n":
            elves.append(elve)
            elve = []
        else:
            elve.append(line.replace("\n", ""))

for i, elve in enumerate(elves):
    total_calory = 0
    for calory in elve:
        total_calory += int(calory)
    elves[i] = total_calory

elves.sort()

print("part 1:", elves[-1])
print("part 2:", elves[-1] + elves[-2] + elves[-3])
