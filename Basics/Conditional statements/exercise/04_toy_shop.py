vacation_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

puzzles_total = puzzles * 2.6
dolls_total = dolls * 3
bears_total = bears * 4.1
minions_total = minions * 8.2
trucks_total = trucks * 2

number_of_toys = puzzles + dolls + bears + minions + trucks
total = puzzles_total + dolls_total + bears_total + minions_total + trucks_total
clean_income = total - total * 0.1

if number_of_toys >= 50:
    clean_income = clean_income - clean_income * 0.25
money_left = 0

if clean_income >= vacation_price:
    money_left = clean_income - vacation_price
    print (f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = vacation_price - clean_income
    print(f"Not enough money! {money_needed:.2f} lv needed.")



