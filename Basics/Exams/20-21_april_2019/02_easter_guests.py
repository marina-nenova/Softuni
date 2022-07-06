from math import ceil
price_per_easter_bread = 4
price_per_egg = 0.45

number_of_guests = int(input())
budget = int(input())

easter_bread_bought = ceil(number_of_guests / 3)
eggs_bought = number_of_guests * 2

total = easter_bread_bought * price_per_easter_bread + eggs_bought * price_per_egg
difference = abs(total - budget)
if total <= budget:
    print(f"Lyubo bought {easter_bread_bought} Easter bread and {eggs_bought} eggs.")
    print(f"He has {difference:.2f} lv. left.")
else:
    print("Lyubo doesn't have enough money.")
    print(f"He needs {difference:.2f} lv. more.")