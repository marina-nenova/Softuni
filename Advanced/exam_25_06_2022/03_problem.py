def shopping_cart(*args):
    products_limits = {"Pizza": 4, "Soup": 3, "Dessert": 2}
    cart = {"Pizza": set(), "Soup": set(), "Dessert": set()}

    for el in args:
        if el == "Stop":
            break
        meal_type = el[0]
        product = el[1]
        if len(cart[meal_type]) < products_limits[meal_type]:
            cart[meal_type].add(product)

    if not cart["Pizza"] and not cart["Soup"] and not cart["Dessert"]:
        return "No products in the cart!"

    result = []

    for meal_type, products in sorted(cart.items(), key= lambda kvpt: (-len(kvpt[1]), kvpt[0])):
        result.append(f"{meal_type}:")
        for product in sorted(products):
            result.append(f" - {product}")

    return '\n'.join(result)


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))

print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
