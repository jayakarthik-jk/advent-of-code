clock = 0
register = 1
strengths = []


def increment_timer():
    global clock
    clock += 1
    if clock == register or clock == register + 1 or clock == register + 2:
        draw("#")
    else:
        draw(".")
    if clock % 40 == 0:
        clock = 0
        print()


def draw(content):
    print(content, end="")


def execute_command(command):
    global register
    match command[0]:
        case "noop":
            increment_timer()
        case "addx":
            increment_timer()
            increment_timer()
            register += int(command[1])


print("part 2:")
with open("app.txt", "r", encoding="UTF-8") as file:
    for line in file:
        execute_command(line.split())
