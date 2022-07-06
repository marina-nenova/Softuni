from math import ceil
wall_hight = int(input())
wall_width = int(input())
percentage_not_to_paint = int(input())
number_of_walls = 4

total_sq_meters = (wall_hight * wall_width) * number_of_walls
to_be_painted = ceil(total_sq_meters - (total_sq_meters * (percentage_not_to_paint / 100)))
all_walls_painted = False

paint_used = 0
command = input()

while command != "Tired!":
    litres_per_sq_meter = int(command)
    paint_used += litres_per_sq_meter
    if paint_used >= to_be_painted:
        all_walls_painted = True
        break
    command = input()

if all_walls_painted:
    if paint_used > to_be_painted:
        paint_left = paint_used - to_be_painted
        print(f"All walls are painted and you have {paint_left} l paint left!")
    elif paint_used == to_be_painted:
        print("All walls are painted! Great job, Pesho!")
else:
    sq_meters_left = to_be_painted - paint_used
    print(f"{sq_meters_left} quadratic m left." )
