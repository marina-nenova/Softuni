budget = float(input())
ticket_type = input()
numbers_of_people = int(input())
price = 0
transport_price = 0

if ticket_type == "VIP":
    price = 499.99

elif ticket_type == "Normal":
    price = 249.99

tickets_price = numbers_of_people * price

if numbers_of_people < 5:
    transport_price = budget * 0.75

elif numbers_of_people < 10:
    transport_price = budget * 0.6

elif numbers_of_people < 25:
    transport_price = budget * 0.5

elif numbers_of_people < 50:
    transport_price = budget * 0.4

else:
    transport_price = budget * 0.25

total = tickets_price + transport_price

if budget >= total:
    money_left = budget - total
    print(f"Yes! You have {money_left:.2f} leva left.")
elif budget < total:
    money_needed = total - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")