number_of_floors = int(input())
number_of_rooms = int(input())
current_floor = ""

for f in range(number_of_floors, 0, -1):
    for r in range(number_of_rooms):
        if f == number_of_floors:
            current_floor += f"L{f}{r} "
        if f % 2 == 1 and f != number_of_floors:
            current_floor += f"A{f}{r} "
        elif f % 2 == 0 and f != number_of_floors:
            current_floor += f"O{f}{r} "

    print(current_floor)
    current_floor = ""