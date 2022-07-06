movie_budget = float(input())
destination = input()
season = input()
number_of_days = int(input())
price_per_day = 0
if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    elif season == "Summer":
        price_per_day = 40000
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    elif season == "Summer":
        price_per_day = 12500
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    elif season == "Summer":
        price_per_day = 20250

total = price_per_day * number_of_days

if destination == "Dubai":
    total -= total * 0.3
elif destination == "Sofia":
    total += total * 0.25

difference = abs(movie_budget - total)
if movie_budget >= total:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")