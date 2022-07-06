championship_stage = input()
ticket_type = input()
number_of_tickets = int(input())
trophy_picture = input()

price_per_ticket = 0
total = 0

if championship_stage == "Quarter final":
    if ticket_type == "Standard":
        price_per_ticket = 55.5
    elif ticket_type == "Premium":
        price_per_ticket = 105.2
    elif ticket_type == "VIP":
        price_per_ticket = 118.9
elif championship_stage == "Semi final":
    if ticket_type == "Standard":
        price_per_ticket = 75.88
    elif ticket_type == "Premium":
        price_per_ticket = 125.22
    elif ticket_type == "VIP":
        price_per_ticket = 300.4
elif championship_stage == "Final":
    if ticket_type == "Standard":
        price_per_ticket = 110.1
    elif ticket_type == "Premium":
        price_per_ticket = 160.66
    elif ticket_type == "VIP":
        price_per_ticket = 400

total = number_of_tickets * price_per_ticket
price_per_picture = 40
if 2500 < total <= 4000:
    total -= total * 0.1
elif total > 4000:
    total -= total * 0.25
    price_per_picture = 0

if trophy_picture == "Y":
    total += number_of_tickets * price_per_picture

print(f"{total:.2f}")