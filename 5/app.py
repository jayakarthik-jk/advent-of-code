# [N]         [C]     [Z]
# [Q] [G]     [V]     [S]         [V]
# [L] [C]     [M]     [T]     [W] [L]
# [S] [H]     [L]     [C] [D] [H] [S]
# [C] [V] [F] [D]     [D] [B] [Q] [F]
# [Z] [T] [Z] [T] [C] [J] [G] [S] [Q]
# [P] [P] [C] [W] [W] [F] [W] [J] [C]
# [T] [L] [D] [G] [P] [P] [V] [N] [R]
#  1   2   3   4   5   6   7   8   9

stacks = [
    ["T", "P", "Z", "C", "S", "L", "Q", "N"],
    ["L", "P", "T", "V", "H", "C", "G"],
    ["D", "C", "Z", "F"],
    ["G", "W", "T", "D", "L", "M", "V", "C"],
    ["P", "W", "C"],
    ["P", "F", "J", "D", "C", "T", "S", "Z"],
    ["V", "W", "G", "B", "D"],
    ["N", "J", "S", "Q", "H", "W"],
    ["R", "C", "Q", "F", "S", "L", "V"],
]

with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file:
        procedure = line.split()
        count = int(procedure[1])
        _from = int(procedure[3]) - 1
        to = int(procedure[5]) - 1
        stacks[to].extend(stacks[_from][len(stacks[_from]) - count :])
        for i in range(count):
            stacks[_from].pop()

for stack in stacks:
    print("part 2:", stack[-1], end="")
