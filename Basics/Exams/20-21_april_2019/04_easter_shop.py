eggs_in_stock = int(input())


command = input()
eggs_sold = 0
not_enough_eggs = False
while command != "Close":
    action = command
    eggs_amount = int(input())
    if eggs_amount > eggs_in_stock and action == "Buy":
        not_enough_eggs = True
        break
    if action == "Buy":
        eggs_in_stock -= eggs_amount
        eggs_sold += eggs_amount
    elif action == "Fill":
        eggs_in_stock += eggs_amount
    command = input()

if not_enough_eggs:
    print("Not enough eggs in store!")
    print(f"You can buy only {eggs_in_stock}.")
else:
    print("Store is closed!")
    print(f"{eggs_sold} eggs sold.")