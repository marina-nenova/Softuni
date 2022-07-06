number_of_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
max_color = ''
for egg in range(number_of_eggs):
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1
max_eggs = 0
if red_eggs > max_eggs:
    max_eggs = red_eggs
    max_color = "red"
if orange_eggs > max_eggs:
    max_eggs = orange_eggs
    max_color = "orange"
if blue_eggs > max_eggs:
    max_eggs = blue_eggs
    max_color = "blue"
if green_eggs > max_eggs:
    max_eggs = green_eggs
    max_color = "green"

print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {max_color}")