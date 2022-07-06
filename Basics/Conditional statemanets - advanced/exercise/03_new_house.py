type_of_flowers = input()
amount = int(input())
budget = int(input())
total = 0
if type_of_flowers == "Roses":
    total = amount * 5
    if amount > 80:
        total -= total * 0.1

elif type_of_flowers == "Dahlias":
    total = amount * 3.8
    if amount > 90:
        total -= total * 0.15

elif type_of_flowers == "Tulips":
    total = amount * 2.8
    if amount > 80:
        total -= total * 0.15

elif type_of_flowers == "Narcissus":
    total = amount * 3
    if amount < 120:
        total = total * 1.15

elif type_of_flowers == "Gladiolus":
    total = amount * 2.5
    if amount < 80:
        total = total * 1.2

if total <= budget:
    money_left = budget - total
    print(f"Hey, you have a great garden with {amount} {type_of_flowers} and {money_left:.2f} leva left.")
elif total > budget:
    money_needed = total - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")