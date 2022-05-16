inheritance = float(input())
final_year = int(input())
expenses = 0
ivan_years = 18

for year in range(1800, final_year + 1):
    if year % 2 == 0:
        expenses += 12000
        ivan_years += 1
    elif year % 2 != 0:
        expenses += 12000 + 50 * ivan_years
        ivan_years += 1
money_left = inheritance - expenses
money_needed = expenses - inheritance
if inheritance >= expenses:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {money_needed:.2f} dollars to survive." )