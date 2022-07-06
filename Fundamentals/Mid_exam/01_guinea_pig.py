# food_kg = float(input())
# hay_kg = float(input())
# cover_kg = float(input())
# guinea_weight_kg = float(input())
# food_grams = food_kg * 1000
# hay_grams = hay_kg * 1000
# cover_grams = cover_kg * 1000
# guinea_weight_grams = guinea_weight_kg * 1000
# enough_supplies = True
#
# for day in range(1, 31):
#     food_grams -= 300
#     if food_grams <= 0:
#         enough_supplies = False
#         break
#     if day % 2 == 0:
#         hay_grams -= food_grams * 0.05
#         if hay_grams <= 0:
#             enough_supplies = False
#             break
#     if day % 3 == 0:
#         cover_grams -= guinea_weight_grams / 3
#         if cover_grams <= 0:
#             enough_supplies = False
#             break
# if enough_supplies:
#     print(f"Everything is fine! Puppy is happy! Food: {(food_grams / 1000):.2f}, Hay: {(hay_grams / 1000):.2f}, Cover: {(cover_grams / 1000):.2f}.")
# else:
#     print("Merry must go to the pet store!")


food_in_kg = float(input())
hay_in_kg = float(input())
cover_in_kg = float(input())
weight = float(input())

food_in_gr = food_in_kg * 1000
hay_in_gr = hay_in_kg * 1000
cover_in_gr = cover_in_kg * 1000
weight_in_gr = weight * 1000
not_enough_supplies = False

for day in range(1, 31):
    food_in_gr -= 300
    if food_in_gr <= 0 or hay_in_gr <= 0 or cover_in_gr <= 0:
        not_enough_supplies = True
        break
    if day % 2 == 0:
        hay_in_gr -= food_in_gr * 0.05
    if day % 3 == 0:
        cover_in_gr -= weight_in_gr / 3

if not_enough_supplies:
    print("Merry must go to the pet store!")
else:
    print(f"Everything is fine! Puppy is happy! Food: {food_in_gr/1000:.2f}, Hay: {hay_in_gr/1000:.2f}, Cover: {cover_in_gr/1000:.2f}.")