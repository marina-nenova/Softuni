type_of_drink = input()
sugar_amount = input()
number_of_drinks = int(input())
price = 0


if type_of_drink == "Espresso":
    if sugar_amount == "Without":
        price = 0.9
    elif sugar_amount == "Normal":
        price = 1
    elif sugar_amount == "Extra":
        price =1.2
elif type_of_drink == "Cappuccino":
    if sugar_amount == "Without":
        price = 1
    elif sugar_amount == "Normal":
        price = 1.2
    elif sugar_amount == "Extra":
        price = 1.6
elif type_of_drink == "Tea":
    if sugar_amount == "Without":
        price = 0.5
    elif sugar_amount == "Normal":
        price = 0.6
    elif sugar_amount == "Extra":
        price = 0.7

total = number_of_drinks * price

if sugar_amount == "Without":
    total -= total * 0.35
if type_of_drink == "Espresso" and number_of_drinks >= 5:
    total -= total * 0.25
if total > 15:
    total -= total * 0.2

print(f"You bought {number_of_drinks} cups of {type_of_drink} for {total:.2f} lv.")