fuel_price = 2.10
tour_gude_price = 100
saturday_discount = 0.1
sunday_discount = 0.2

budget = float(input())
litres_fuel_needed = float(input())
day_of_week = input()

total_for_fuel = litres_fuel_needed * fuel_price
total_before_discount = total_for_fuel + tour_gude_price
final_total = total_before_discount
if day_of_week == "Saturday":
    final_total -= final_total * saturday_discount
elif day_of_week == "Sunday":
    final_total -= final_total * sunday_discount

difference = abs(final_total - budget)
if final_total <= budget:
    print(f"Safari time! Money left: {difference:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {difference:.2f} lv.")