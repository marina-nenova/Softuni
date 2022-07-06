budget = int(input())
season = input()
number_of_fishermen = int(input())
total = 0

if season == "Spring":
    price = 3000
    if number_of_fishermen <= 6:
        total = price - (price * 0.1)
    elif 7 < number_of_fishermen <= 11:
        total = price - (price * 0.15 )
    elif number_of_fishermen > 12:
        total = price - (price * 0.25)

elif season in "Summer Autumn":
    price = 4200
    if number_of_fishermen <= 6:
        total = price - (price * 0.1)
    elif 7 < number_of_fishermen <= 11:
        total = price - (price * 0.15)
    elif number_of_fishermen > 12:
        total = price - (price * 0.25)


elif season == "Winter":
    price = 2600
    if number_of_fishermen <= 6:
        total = price - (price * 0.1)
    elif 7 < number_of_fishermen <= 11:
        total = price - (price * 0.15)
    elif number_of_fishermen > 12:
        total = price - (price * 0.25)

if season != "Autumn" and number_of_fishermen %2 == 0:
    total -= total * 0.05

if budget >= total:
    money_left = budget - total
    print(f"Yes! You have {money_left:.2f} leva left.")
elif budget < total:
    money_needed = total - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")