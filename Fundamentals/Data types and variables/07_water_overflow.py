tank_capacity = 255
number_of_lines = int(input())
litres_in_tank = 0
for litres in range(number_of_lines):
    litres_water = int(input())
    if litres_water > tank_capacity:
        print("Insufficient capacity!")
        continue
    litres_in_tank += litres_water
    tank_capacity -= litres_water
print(litres_in_tank)