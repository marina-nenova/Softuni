import math

magnolias = int(input())
hyacinth = int(input())
roses = int(input())
cacti = int(input())
present = float(input())

income = magnolias * 3.25 + hyacinth * 4 + roses * 3.5 + cacti * 8
clean_income = income - (income * 0.05)

if clean_income >= present:
    money_left = math.floor(clean_income - present)
    print(f"She is left with {money_left} leva.")
else:
    money_needed = math.ceil(present - clean_income)
    print(f"She will have to borrow {money_needed} leva." )