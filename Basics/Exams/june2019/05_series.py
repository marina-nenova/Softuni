budget = float(input())
number_of_series = int(input())
total = 0

for series in range(number_of_series):
    name_of_series = input()
    price_per_series = float(input())
    if name_of_series == "Thrones":
        price_per_series -= price_per_series * 0.5
    elif name_of_series == "Lucifer":
        price_per_series -= price_per_series * 0.4
    elif name_of_series == "Protector":
        price_per_series -= price_per_series * 0.3
    elif name_of_series == "TotalDrama":
        price_per_series -= price_per_series * 0.2
    elif name_of_series == "Area":
        price_per_series -= price_per_series * 0.1
    total += price_per_series

difference = abs(budget - total)
if budget >= total:
    print(f"You bought all the series and left with {difference:.2f} lv.")
else:
    print(f"You need {difference:.2f} lv. more to buy the series!")