x = float(input())
y = float(input())
h = float(input())

walls = (x * y) * 2
window = 1.5 * 1.5
both_walls = walls - 2 * window

door = 1.2 * 2
front_wall = x * x - door
back_wall = x * x
front_and_back = front_wall + back_wall

total_area_house = both_walls + front_and_back

green_paint = total_area_house / 3.4
print(f"{green_paint:.2f}")

roof_walls = walls
roof_triangles = 2 * (x * h / 2)
total_area_roof = roof_walls + roof_triangles
red_paint = total_area_roof / 4.3
print(f"{red_paint:.2f}")