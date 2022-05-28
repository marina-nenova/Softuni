def stock_availability (inventory, action, *args):

    if action == "delivery":
        inventory.extend(list(args))

    elif action == "sell":
        if not args:
            inventory = inventory[1:]
        else:
            for el in args:
                try:
                    inventory = inventory[el:]
                except:
                    inventory = [ingredient for ingredient in inventory if ingredient != el]
    return inventory


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
