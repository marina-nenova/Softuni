possible_moves = {"up left": (row - 1, col - 1), "up": (row - 1, col), "up right": (row - 1, col + 1), "right": (row, col + 1),
                      "left": (row + 1, col - 1), "down": (row + 1, col), "down right":(row + 1, col + 1), "down left":(row, col - 1)}

possible_positions = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1), (row, col + 1),
                      (row + 1, col + 1), (row + 1, col), (row + 1, col - 1), (row, col - 1)]

possible_moves = {"up": (row - 1, col), "right": (row, col + 1), "down": (row + 1, col), "left": (row, col - 1)}

possible_moves = [(row - 1, col), (row, col + 1), (row + 1, col), (row, col - 1)]


def valid_coordinates(row_index, col_index, size):
    return 0 <= row_index < size and 0 <= col_index < size

while True:
    if current_direction == "up":
        row_index -= 1
    elif current_direction == "down":
        row_index += 1
    elif current_direction == "left":
        col_index -= 1
    elif current_direction == "right":
        col_index += 1



    while True:
        if direction == "up left":
            row, col = row - 1, col - 1
        elif direction == "up":
            row, col = row - 1, col
        elif direction == "up right":
            row, col = row - 1, col + 1
        elif direction == "right":
            row, col = row, col + 1
        elif direction == "left":
            row, col = row + 1, col - 1
        elif direction == "down":
            row, col = row + 1, col
        elif direction == "down right":
            row, col = row + 1, col + 1
        elif direction == "down left":
            row, col = row, col - 1


def next_position(row_index, col_index, current_direction, steps):
    steps_made = []

    for step in range(steps):

        if current_direction == "up":
            row_index = rows - 1 if row_index == 0 else row_index - 1
        elif current_direction == "down":
            row_index = 0 if row_index == rows - 1 else row_index + 1
        elif current_direction == "left":
            col_index = cols - 1 if col_index == 0 else col_index - 1
        elif current_direction == "right":
            col_index = 0 if col_index == cols - 1 else col_index + 1

        steps_made.append((row_index, col_index))

    return steps_made


def next_position(row_index, col_index, current_direction):
    if current_direction == "up":
        row_index = size - 1 if row_index == 0 else row_index - 1
    elif current_direction == "down":
        row_index = 0 if row_index == size - 1 else row_index + 1
    elif current_direction == "left":
        col_index = size - 1 if col_index == 0 else col_index - 1
    elif current_direction == "right":
        col_index = 0 if col_index == size - 1 else col_index + 1

    return row_index, col_index


directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'down': lambda r, c: (r + 1, c),
    'up': lambda r, c: (r - 1, c)
}

row, col = directions[direction](alice_row, alice_col)