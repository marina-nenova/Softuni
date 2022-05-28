def get_magic_triangle(n):

    magic_triangle = []
    starting_num = 1

    for row in range(n):
        current_row = []

        for index in range(row + 1):
            if index == 0 or index == row:
                current_row.append(starting_num)
            else:
                previous_row = magic_triangle[row - 1]
                current_row.append(previous_row[index - 1] + previous_row[index])
        magic_triangle.append(current_row)
    return magic_triangle



print(get_magic_triangle(7))