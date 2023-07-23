grid: list[list[int]] = []
with open("input.txt", "r", encoding="UTF-8") as file:
    for line in file:
        row = []
        for i in range(len(line.strip())):
            row.append(int(line[i]))
        grid.append(row)

counter = 0
ROW_COUNT = len(grid)
COL_COUNT = len(grid[0])
for i in range(ROW_COUNT):
    for j in range(COL_COUNT):
        val = grid[i][j]
        if i == 0 or j == 0 or i == ROW_COUNT - 1 or j == COL_COUNT - 1:
            counter += 1
            continue
        # left
        for k in range(j - 1, -1, -1):
            if grid[i][k] >= val:
                break
        else:
            counter += 1
            continue
        # right
        for k in range(j + 1, COL_COUNT):
            if grid[i][k] >= val:
                break
        else:
            counter += 1
            continue
        # top
        for k in range(i - 1, -1, -1):
            if grid[k][j] >= val:
                break
        else:
            counter += 1
            continue
        # bottom
        for k in range(i + 1, ROW_COUNT):
            if grid[k][j] >= val:
                break
        else:
            counter += 1
            continue


print("part 1:", counter)

max_scenic = 0
for i in range(ROW_COUNT):
    for j in range(COL_COUNT):
        total_scenic = 1
        scenic = 0

        val = grid[i][j]
        if i == 0 or j == 0 or i == ROW_COUNT - 1 or j == COL_COUNT - 1:
            continue
        # left
        for k in range(j - 1, -1, -1):
            scenic += 1
            if grid[i][k] >= val:
                break
        total_scenic *= scenic
        scenic = 0
        # right
        for k in range(j + 1, COL_COUNT):
            scenic += 1
            if grid[i][k] >= val:
                break
        total_scenic *= scenic
        scenic = 0
        # top
        for k in range(i - 1, -1, -1):
            scenic += 1
            if grid[k][j] >= val:
                break
        total_scenic *= scenic
        scenic = 0
        # bottom
        for k in range(i + 1, ROW_COUNT):
            scenic += 1
            if grid[k][j] >= val:
                break
        total_scenic *= scenic
        scenic = 0
        if total_scenic > max_scenic:
            max_scenic = total_scenic

print("part 2:", max_scenic)
