def shopping_list(budget, **kwargs):
    output = ""
    basket_capacity = 5
    if budget < 100:
        return "You do not have enough budget."
    for product, info in kwargs.items():
        price = info[0]
        quantity = info[1]
        total = price * quantity
        if total <= budget:
            budget -= total
            basket_capacity -= 1
            output += f"You bought {product} for {total:.2f} leva.\n"
        if basket_capacity == 0:
            break
    return output


print(shopping_list(100,
                    microwave=(70, 2),
                    skirts=(15, 4),
                    coffee=(1.50, 10),
                    ))

print(shopping_list(20,
                    jeans=(19.99, 1),
                    ))

print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
