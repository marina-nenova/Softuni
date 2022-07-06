flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
egg_cartons = int(input())
yeast = int(input())

sugar_price = flour_price - (flour_price * 0.25)
egg_carton_price = flour_price + (flour_price * 0.1)
yeast_price = sugar_price - (sugar_price * 0.8)

total = flour_kg * flour_price + sugar_kg * sugar_price + yeast * yeast_price + egg_cartons * egg_carton_price

print(f"{total:.2f}")