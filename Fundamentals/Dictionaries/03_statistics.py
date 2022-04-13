command = input()

stock = {}
while not command == "statistics":
    product, quantity = command.split(":")
    if product not in stock:
        stock[product] = int(quantity)
    else:
        stock[product] += int(quantity)
    command = input()

print("Products in stock:")

for product, quantity in stock.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(stock)}")
print(f"Total Quantity: {sum(stock.values())}")
