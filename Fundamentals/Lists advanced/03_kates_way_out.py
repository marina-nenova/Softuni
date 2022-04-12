def find_next(coordinates, maze):
    next_coordinates = []
    if coordinates[0] - 1 >= 0 and maze[coordinates[0] - 1][coordinates[1]] != "#":  # check up and if first row
        next_coordinates.append((coordinates[0] - 1, coordinates[1]))
    if coordinates[0] + 1 < len(maze) and maze[coordinates[0] + 1][coordinates[1]] != "#":  # check down
        next_coordinates.append((coordinates[0] + 1, coordinates[1]))
    if coordinates[1] + 1 < len(maze[0]) and maze[coordinates[0]][coordinates[1] + 1] != "#":  # check right
        next_coordinates.append((coordinates[0], coordinates[1] + 1))
    if coordinates[1] - 1 >= 0 and maze[coordinates[0]][coordinates[1] - 1] != "#":  # check left and if first column
        next_coordinates.append((coordinates[0], coordinates[1] - 1))
    return next_coordinates


def dfs(maze, stack, visited, start, goals):
    way_out_found = False
    stack.append(start)
    visited.add(start)
    most_moves = 0

    for goal in goals:
        while stack:
            n = stack.pop()
            if n == goal:                   # checks if goal
                way_out_found = True

            next_steps = find_next(n, maze)  # sends coordinate to function to find next available moves

            for x in next_steps:
                if x in visited:             # checks if visited
                    continue
                visited.add(x)
                stack.append(x)

    moves = len(visited)
    if moves >= most_moves:
        most_moves = moves
    if way_out_found:
        print(f"Kate got out in {most_moves} moves")
    else:
        print("Kate cannot get out")


rows = int(input())
maze = []
start = ()
goals = []
for row in range(rows):
    maze.append(list(input()))

for row in range(len(maze)):
    for col in range(len(maze[0])):
        if maze[row][col] == "k":
            start = (row, col)
for row in range(rows):
    for col in range(len(maze[row])):
        if (maze[row][col] == " " or maze[row][col] == "k") and (            # Check if there's an empty space on first, last column or last row
                row == rows - 1 or col == 0 or col == len(maze[1]) - 1):     # Kate cannot get out from the first row
            goals.append((row, col))

stack = []
visited = set()
dfs(maze, stack, visited, start, goals)
