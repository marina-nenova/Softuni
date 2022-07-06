stock = input().split()
searched_products = input().split()
products = {}

for index in range(0, len(stock), 2):
    key = stock[index]
    value = int(stock[index + 1])
    products[key] = value

for s_p in searched_products:
    if s_p in products:
        print(f"We have {products[s_p]} of {s_p} left")
    else:
        print(f"Sorry, we don't have {s_p}")