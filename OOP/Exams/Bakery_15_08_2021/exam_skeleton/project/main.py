from project.bakery import Bakery

bakery = Bakery("Sunny")
print(bakery.add_food("Bread", "Sour", 1.50))
print(bakery.add_food("Bread", "White", 1.30))
print(bakery.add_food("Cake", "Chocolate", 2.90))
print(bakery.add_food("Cake", "Vanilla", 2.90))

print(bakery.add_drink("Water", "Spring", 250, "Bankya"))
print(bakery.add_drink("Water", "Mineral", 500, "Devin"))
print(bakery.add_drink("Tea", "Black", 250, "Ahmad Tea"))
print(bakery.add_drink("Tea", "Green", 250, "Lipton"))

print(bakery.add_table("OutsideTable", 52, 10))
print(bakery.add_table("OutsideTable", 95, 15))
print(bakery.add_table("InsideTable", 15, 15))
print(bakery.add_table("InsideTable", 4, 15))

print(bakery.reserve_table(12))
print(bakery.order_food(95, "Sour", "White", "Chocolate", "Vanilla", "Strawberry", "Hazelnut", "Wholegrain"))
print(bakery.order_drink(95, "Spring", "Mineral", "Black", "Green", "White", "Tap", "Fruit"))
print(bakery.leave_table(95))
print(bakery.total_income)
print(bakery.get_free_tables_info())
print(bakery.get_total_income())