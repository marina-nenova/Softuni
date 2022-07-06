eggs_size = input()
eggs_color = input()
number_of_eggs_pack = int(input())
price_per_eggs_pack = 0
expenses_percentage = 0.35
if eggs_size == "Large":
    if eggs_color == "Red":
        price_per_eggs_pack = 16
    elif eggs_color == "Green":
        price_per_eggs_pack = 12
    elif eggs_color == "Yellow":
        price_per_eggs_pack = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        price_per_eggs_pack = 13
    elif eggs_color == "Green":
        price_per_eggs_pack = 9
    elif eggs_color == "Yellow":
        price_per_eggs_pack = 7
elif eggs_size == "Small":
    if eggs_color == "Red":
        price_per_eggs_pack = 9
    elif eggs_color == "Green":
        price_per_eggs_pack = 8
    elif eggs_color == "Yellow":
        price_per_eggs_pack = 5

income = number_of_eggs_pack * price_per_eggs_pack
expenses = income * expenses_percentage
profit = income - expenses

print(f"{profit:.2f} leva.")