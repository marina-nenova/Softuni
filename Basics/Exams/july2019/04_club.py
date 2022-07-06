profit_target = float(input())
total = 0
command = input()
profit_target_reached = False
while command != "Party!":
    cocktail_name = command
    number_of_cocktails = int(input())
    price_per_cocktail = len(cocktail_name)
    total_order = number_of_cocktails * price_per_cocktail
    if total_order % 2 == 1:
        total_order -= total_order * 0.25
    total += total_order
    if total >= profit_target:
        profit_target_reached = True
        break
    command = input()
if profit_target_reached:
    print("Target acquired.")
else:
    money_needed = profit_target - total
    print(f"We need {money_needed:.2f} leva more.")
print(f"Club income - {total:.2f} leva.")