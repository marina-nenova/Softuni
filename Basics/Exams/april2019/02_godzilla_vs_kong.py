movie_budget = float(input())
number_of_extras = int(input())
costume_price = float(input())

decor = 0.1 * movie_budget

all_costumes_price = number_of_extras * costume_price

if number_of_extras > 150:
    all_costumes_price -= all_costumes_price * 0.1

total_expences = all_costumes_price + decor

difference = abs(total_expences - movie_budget)

if total_expences > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")