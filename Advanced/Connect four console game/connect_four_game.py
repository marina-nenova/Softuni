from ascii_art import connect_four_logo

class InvalidColumnError(Exception):
    pass


class FullColumnError(Exception):
    pass


def print_matrix(matrix):
    # print matrix
    for row in matrix:
        print(row)


def valid_coordinates(row, col, rows, cols):
    return 0 <= row < rows and 0 <= col < cols


def validate_column_choice(col_choice, max_col_index):
    # verify player choice of column is valid
    if not 0 <= col_choice <= max_col_index:
        raise InvalidColumnError


def place_player_choice(matrix, selected_col_index, rows_count, player_num):
    # Place player marker on column. If column is full throw an error.
    for row in range(rows_count - 1, -1, -1):
        if matrix[row][selected_col_index] == 0:
            matrix[row][selected_col_index] = player_num
            return row, selected_col_index
    raise FullColumnError


def check_horizontal(matrix, row, col, player_num):
    player_positions = [(row, col)]
    current_col = col
    while True:
        current_col -= 1
        if valid_coordinates(row, current_col, rows, cols) and matrix[row][current_col] == player_num:
            player_positions.append((row, current_col))
        else:
            break

    current_col = col
    while True:
        current_col += 1
        if valid_coordinates(row, current_col, rows, cols) and matrix[row][current_col] == player_num:
            player_positions.append((row, current_col))
        else:
            break
    return player_positions


def check_right_diagonal(matrix, row, col, player_num):
    player_positions = [(row, col)]
    current_row = row
    current_col = col
    while True:
        current_row -= 1
        current_col += 1
        if valid_coordinates(current_row, current_col, rows, cols) and matrix[current_row][current_col] == player_num:
            player_positions.append((current_row, current_col))
        else:
            break

    current_col = col
    current_row = row
    while True:
        current_row += 1
        current_col -= 1
        if valid_coordinates(current_row, current_col, rows, cols) and matrix[current_row][current_col] == player_num:
            player_positions.append((current_row, current_col))
        else:
            break
    return player_positions


def check_left_diagonal(matrix, row, col, player_num):
    player_positions = [(row, col)]
    current_row = row
    current_col = col
    while True:
        current_row -= 1
        current_col -= 1
        if valid_coordinates(current_row, current_col, rows, cols) and matrix[current_row][current_col] == player_num:
            player_positions.append((current_row, current_col))
        else:
            break

    current_col = col
    current_row = row
    while True:
        current_row += 1
        current_col += 1
        if valid_coordinates(current_row, current_col, rows, cols) and matrix[current_row][current_col] == player_num:
            player_positions.append((current_row, current_col))
        else:
            break
    return player_positions


def check_down(matrix, row, col, player_num):
    player_positions = [(row, col)]
    current_row = row
    current_col = col
    while True:
        current_row -= 1
        if valid_coordinates(current_row, current_col, rows, cols) and matrix[current_row][current_col] == player_num:
            player_positions.append((current_row, current_col))
        else:
            break
    return player_positions


def is_winner(matrix, row, col, player_num):
    if len(check_horizontal(matrix, row, col, player_num)) >= 4 or \
            len(check_right_diagonal(matrix, row, col, player_num)) >= 4 or \
            len(check_left_diagonal(matrix, row, col, player_num)) >= 4 or \
            len(check_down(matrix, row, col, player_num)) >= 4:
        return True
    return False


rows = 6
cols = 7
# create matrix:
matrix = [[0 for col in range(cols)] for row in range(rows)]

player_num = 1
print(connect_four_logo)
while True:
    player_num = 2 if player_num % 2 == 0 else 1
    try:
        # read column choice
        column_num = int(input(f"Player {player_num}, please choose a column. ")) - 1
        validate_column_choice(column_num, cols - 1)
        row, col = place_player_choice(matrix, column_num, rows, player_num)
        if is_winner(matrix, row, col, player_num):
            print(f"The winner is Player {player_num}")
            break
        print_matrix(matrix)
    except InvalidColumnError:
        print(f"This column is not valid. Please select a number between {1} and {cols}.")
        continue
    except ValueError:
        print("Please select a valid integer!")
        continue
    except FullColumnError:
        print(f"Column {column_num + 1} is full. Please choose a different column.")
        continue

    player_num += 1
