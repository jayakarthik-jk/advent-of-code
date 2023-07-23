class Folder:
    def __init__(self, name):
        self.name = name
        self.children: list[Folder] = []
        self.size = 0
        self.type = "folder"


class File:
    def __init__(self, file_name: str, file_size: int):
        self.name = file_name
        self.size = file_size


with open("input.txt", "r", encoding="UTF-8") as file:
    path: list[Folder] = []
    for line in file:
        command = line.split()
        if command[0] == "$":
            if command[1] == "cd":
                if command[2] == "..":
                    path.pop()
                elif command[2] == "/":
                    folder = Folder(command[2])
                    path.append(folder)
                else:
                    for child in path[-1].children:
                        if isinstance(child, Folder) and child.name == command[2]:
                            path.append(child)
                            break
        elif command[0] == "dir":
            folder = Folder(command[1])
            path[-1].children.append(folder)
        else:
            size = int(command[0])
            file = File(command[1], size)
            for parent in path:
                parent.size += size
            path[-1].children.append(file)
    root = path[0]


stack: list[Folder] = [root]
count = 0
while len(stack) != 0:
    folder = stack.pop()
    for child in folder.children:
        if isinstance(child, Folder):
            stack.append(child)
    if folder.size < 100_000:
        count += folder.size
print("part 1: ", count)

TOTAL_SPACE = 70_000_000
USED_SPACE = root.size
NEEDED_SPACE = 30_000_000
AVAILABLE_SPACE = TOTAL_SPACE - USED_SPACE
SHORTAGE_SPACE = NEEDED_SPACE - AVAILABLE_SPACE

best = root.size
stack: list[Folder] = [root]
while len(stack) != 0:
    folder = stack.pop()
    for child in folder.children:
        if isinstance(child, Folder):
            stack.append(child)
    if folder.size > SHORTAGE_SPACE and folder.size < best:
        best = folder.size

print("part 2:", best)
