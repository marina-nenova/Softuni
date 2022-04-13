stock = input().split()
products = {}

for index in range(0, len(stock), 2):
    key = stock[index]
    value = int(stock[index + 1])
    products[key] = value

print(products)