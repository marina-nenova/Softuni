movie_budget = float(input())
extras = int(input())
costume_price = float(input())

decor = movie_budget * 0.1

if extras > 150:
    all_costumes = (extras * costume_price) * 0.9
else:
    all_costumes = extras * costume_price

total_expenses = decor + all_costumes

if total_expenses > movie_budget:
    money_needed = total_expenses - movie_budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = movie_budget - total_expenses
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")