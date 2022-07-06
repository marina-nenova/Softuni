budget = float(input())
nights = int(input())
price_per_night = float(input())
other_expenses_percentage = int(input())

if nights > 7:
    price_per_night -= price_per_night * 0.05

hotel_expenses = nights * price_per_night
other_expenses = (other_expenses_percentage / 100) * budget
total_expenses = hotel_expenses + other_expenses

difference = abs(total_expenses - budget)
if total_expenses <= budget:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")