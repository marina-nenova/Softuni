def fill_the_box(height, length, width, *args):
    capacity = height * length * width
    cubes_left = 0
    for el in args:
        if el == "Finish":
            break
        if el > capacity:
            el -= capacity
            cubes_left += el
            capacity = 0
        else:
            capacity -= el

    if capacity > 0:
        return f"There is free space in the box. You could put {capacity} more cubes."
    else:
        return f"No more free space! You have {cubes_left} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))

print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))