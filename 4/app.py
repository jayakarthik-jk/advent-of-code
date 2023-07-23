count = 0
with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file:
        p1, p2 = line.replace("\n", "").split(",")
        p1, p2 = p1.split("-"), p2.split("-")
        p1[0] = int(p1[0])
        p1[1] = int(p1[1])
        p2[0] = int(p2[0])
        p2[1] = int(p2[1])
        if p1[0] <= p2[0] and p1[1] >= p2[1]:
            count += 1
        elif p1[0] >= p2[0] and p1[1] <= p2[1]:
            count += 1
print("part 1:", count)


count = 0
with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file:
        p1, p2 = line.replace("\n", "").split(",")
        p1, p2 = p1.split("-"), p2.split("-")
        p1[0] = int(p1[0])
        p1[1] = int(p1[1])
        p2[0] = int(p2[0])
        p2[1] = int(p2[1])
        if p1[0] <= p2[0] and p2[0] <= p1[1]:
            count += 1
        elif p1[0] <= p2[1] and p2[1] <= p1[1]:
            count += 1
        elif p2[0] <= p1[0] and p1[0] <= p2[1]:
            count += 1
        elif p2[0] <= p1[1] and p1[1] <= p2[1]:
            count += 1
print("part 2:", count)
