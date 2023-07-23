total_priority = 0
ALPHA = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file.readlines():
        rucksack = line.replace("\n", "")
        l = len(rucksack) // 2
        c1 = set(rucksack[:l])
        c2 = set(rucksack[l:])
        (c,) = c1.intersection(c2)
        total_priority += ALPHA.index(c) + 1
print("part 1:", total_priority)


with open("input.txt", "r", encoding="UTF-8") as file:
    index, count = 0, 0
    groups: list[list[str]] = []
    for i, line in enumerate(file.readlines()):
        rucksack = line.replace("\n", "")
        if count == 0:
            groups.append([rucksack])
            count += 1
        elif count == 1:
            groups[index].append(rucksack)
            count += 1
        elif count == 2:
            groups[index].append(rucksack)
            count = 0
            index += 1

priority = 0
for group in groups:
    (r,) = set(group[0]).intersection(group[1]).intersection(group[2])
    priority += ALPHA.index(r) + 1

print("part 2:", priority)
