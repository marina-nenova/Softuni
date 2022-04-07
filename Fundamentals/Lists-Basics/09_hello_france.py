import decimal

items = input().split("|")
budget = float(input())
ticket_cost = 150
items_new_prices = []
data_prices = []
profit = 0

for item in items:
    item_specifics = item.split("->")
    item_type = item_specifics[0]
    item_price = float(item_specifics[1])
    if item_type == "Clothes":
        if item_price > 50:
            continue
    elif item_type == "Shoes":
        if item_price > 35:
            continue
    elif item_type == "Accessories":
        if item_price > 20.5:
            continue
    if budget < item_price:
        continue
    budget -= item_price
    profit_per_item = item_price * 0.4
    profit += profit_per_item
    new_price = item_price + profit_per_item
    items_new_prices.append(new_price)
    data_prices.append(f"{new_price:.2f}")


sum_collected = sum(items_new_prices) + budget

print(*data_prices)
print(f"Profit: {profit:.2f}")

if sum_collected >= ticket_cost:
    print("Hello, France!")
else:
    print("Not enough money.")
