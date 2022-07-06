import math
price_per_racket = float(input())
number_of_rackets = int(input())
pairs_of_shoes = int(input())

price_per_shoes = price_per_racket / 6
total_for_rackets_and_shoes = number_of_rackets * price_per_racket + pairs_of_shoes * price_per_shoes

other_equipment_price = total_for_rackets_and_shoes * 0.2

total = total_for_rackets_and_shoes + other_equipment_price

paid_by_player = math.floor(total / 8)
paid_by_sponsors = math.ceil((total * 7) / 8)

print(f"Price to be paid by Djokovic {paid_by_player}")
print(f"Price to be paid by sponsors {paid_by_sponsors}")