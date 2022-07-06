budget = float(input())
command = input()
products_bought = 0
money_spent = 0
budget_spent = False

while command != "Stop":
    product = command
    product_price = float(input())
    products_bought += 1
    if products_bought % 3 == 0:
        product_price /= 2
    money_spent += product_price
    if money_spent > budget:
        budget_spent = True
        break
    command = input()

if budget_spent:
    money_needed = money_spent - budget
    print("You don't have enough money!")
    print(f"You need {money_needed:.2f} leva!")
else:
    print(f"You bought {products_bought} products for {money_spent:.2f} leva.")