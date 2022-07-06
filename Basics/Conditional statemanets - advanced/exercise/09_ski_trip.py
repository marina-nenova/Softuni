days_stay = int(input())
type_of_room = input()
rating = input()
total = 0
price = 0
discount = 0
if type_of_room == "room for one person":
    price = 18

elif type_of_room == "apartment":
    price = 25
    if days_stay < 10:
        discount = 0.3
    elif days_stay <= 15:
        discount = 0.35
    elif days_stay > 15:
        discount = 0.5

elif type_of_room == "president apartment":
    price = 35
    if days_stay < 10:
        discount = 0.1
    elif days_stay <= 15:
        discount = 0.15
    elif days_stay > 15:
        discount = 0.2

total = (days_stay - 1) * price - ((days_stay - 1) * price) * discount

if rating == "positive":
    total += total * 0.25
elif rating == "negative":
    total -= total * 0.1

print(f"{total:.2f}")