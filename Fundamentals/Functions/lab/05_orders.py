def price_calculator(item, quantity):
    if item == "coffee":
        return quantity * 1.5
    elif item == "coke":
        return quantity * 1.4
    elif item == "water":
        return quantity * 1
    elif item == "snacks":
        return quantity * 2


product = input()
number_of_products = int(input())

result = price_calculator(product, number_of_products)
print(f"{result:.2f}")