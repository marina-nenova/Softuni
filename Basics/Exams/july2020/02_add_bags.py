bags_price_over_20_kg = float(input())
bags_kg = float(input())
days_left = int(input())
number_of_bags = int(input())
bags_price = 0
if bags_kg < 10:
    bags_price = bags_price_over_20_kg * 0.2
elif 10 <= bags_kg <= 20:
    bags_price = bags_price_over_20_kg * 0.5
elif bags_kg > 20:
    bags_price = bags_price_over_20_kg

total = number_of_bags * bags_price
if days_left > 30:
    total += total * 0.1
elif 7 <= days_left <= 30:
    total += total * 0.15
elif days_left < 7:
    total += total * 0.4

print(f" The total price of bags is: {total:.2f} lv. ")
