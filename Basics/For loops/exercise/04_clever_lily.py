lily_age = int(input())
washer_price = float(input())
toy_price = int(input())
total_money_from_gifts = 0
toys = 0
money_per_year = 0
brother_money = 0
for i in range(1, lily_age + 1):
    if i % 2 == 0:
        money_per_year += 10
        total_money_from_gifts += money_per_year
        brother_money += 1
    else:
        toys += 1
money_from_toys = toys * toy_price
total_saved = total_money_from_gifts - brother_money + money_from_toys

difference = abs(total_saved - washer_price)
if total_saved >= washer_price:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")
