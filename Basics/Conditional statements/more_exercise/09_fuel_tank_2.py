type_fuel = input()
amount = float(input())
club_card = input()

if club_card == "Yes":
    discount = 0
    if type_fuel == "Gasoline":
        discount = 0.18
        total = amount * (2.22 - discount)
    elif type_fuel == "Diesel":
        discount = 0.12
        total = amount * (2.33 - discount)
    elif type_fuel == "Gas":
        discount = 0.08
        total = amount * (0.93 - discount)

elif club_card == "No":
    if type_fuel == "Gasoline":
        total = amount * 2.22
    elif type_fuel == "Diesel":
        total = amount * 2.33
    elif type_fuel == "Gas":
        total = amount * 0.93

if 20 <= amount <= 25:
    total -= total * 0.08
elif amount > 25:
    total -= total * 0.1

print(f"{total:.2f} lv.")



