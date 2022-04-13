command = input()
products_dict = {}
while not command == "buy":
    product, price, quantity = command.split()

    if product not in products_dict:
        products_dict[product] = []
        products_dict[product].append(float(price))
        products_dict[product].append(int(quantity))
    else:
        products_dict[product][0] = float(price)
        products_dict[product][1] += int(quantity)

    command = input()
products_dict = {key: value[0] * value[1] for key, value in products_dict.items()}

for product, total in products_dict.items():
    print(f"{product} -> {total:.2f}")
