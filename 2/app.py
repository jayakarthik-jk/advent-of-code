score = 0
with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file.readlines():
        op, me = line.replace("\n", "").split(" ")
        if me == "X":
            if op == "A":
                score += 3 + 1
            if op == "B":
                score += 0 + 1
            if op == "C":
                score += 6 + 1

        if me == "Y":
            if op == "A":
                score += 6 + 2
            if op == "B":
                score += 3 + 2
            if op == "C":
                score += 0 + 2

        if me == "Z":
            if op == "A":
                score += 0 + 3
            if op == "B":
                score += 6 + 3
            if op == "C":
                score += 3 + 3


print("part 1: ", score)

with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file.readlines():
        op, me = line.replace("\n", "").split(" ")
        if me == "X":
            if op == "A":
                score += 0 + 3
            if op == "B":
                score += 0 + 1
            if op == "C":
                score += 0 + 2

        if me == "Y":
            if op == "A":
                score += 3 + 1
            if op == "B":
                score += 3 + 2
            if op == "C":
                score += 3 + 3

        if me == "Z":
            if op == "A":
                score += 6 + 2
            if op == "B":
                score += 6 + 3
            if op == "C":
                score += 6 + 1
print("part 2:", score)
