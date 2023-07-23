def update_knot(head, tail, visited, knots):
    if abs(head[0] - tail[0]) >= 2 or abs(head[1] - tail[1]) >= 2:
        match (head[0] - tail[0], head[1] - tail[1]):
            case (0, -2):
                decision = (0, -1)
            case (0, 2):
                decision = (0, 1)
            case (2, 0):
                decision = (1, 0)
            case (-2, 0):
                decision = (-1, 0)
            case (1, 2) | (2, 1) | (2, 2):
                decision = (1, 1)
            case (1, -2) | (2, -1) | (2, -2):
                decision = (1, -1)
            case (-1, 2) | (-2, 1) | (-2, 2):
                decision = (-1, 1)
            case (-1, -2) | (-2, -1) | (-2, -2):
                decision = (-1, -1)
        tail[0] += decision[0]
        tail[1] += decision[1]
        update_space(visited, knots)
    return tail


def execute_command(command, knots, visited):
    direction, step = command[0], int(command[1])
    match direction:
        case "U":
            position = (0, -1)
        case "D":
            position = (0, 1)
        case "L":
            position = (1, -1)
        case "R":
            position = (1, 1)
    for _ in range(step):
        knots[0][position[0]] += position[1]
        for j in range(1, len(knots)):
            knots[j] = update_knot(knots[j - 1], knots[j], visited, knots)


def update_space(visited, knots):
    if is_visited(visited, knots):
        return
    visited.append(knots[-1].copy())


def is_visited(visited, knots):
    for i in range(len(visited) - 1, -1, -1):
        if knots[-1][0] == visited[i][0] and knots[-1][1] == visited[i][1]:
            return True
    return False


def execute(knots, visited):
    with open("input.txt", "r", encoding="UTF-8") as file:
        for line in file:
            execute_command(line.split(), knots, visited)


p1knots = []
for _ in range(2):
    p1knots.append([0, 0])
p1visited = [[0, 0]]
execute(p1knots, p1visited)
print("part 1: ", len(p1visited))

p2knots = []
for _ in range(10):
    p2knots.append([0, 0])
p2visited = [[0, 0]]
execute(p2knots, p2visited)
print("part 2: ", len(p2visited))
