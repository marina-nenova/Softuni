import math
number_of_days = int(input())
food_in_kg = int(input())
food_per_dog_kg = float(input())
food_per_cat_kg = float(input())
food_per_turtle_gr = float(input())

dog_needs = food_per_dog_kg * number_of_days
cat_needs = food_per_cat_kg * number_of_days
turtle_needs = (food_per_turtle_gr / 1000) * number_of_days

total_food_needed = dog_needs + cat_needs + turtle_needs

if total_food_needed <= food_in_kg:
    food_left = math.floor(food_in_kg - total_food_needed)
    print(f"{food_left} kilos of food left.")
else:
    food_needed = math.ceil(total_food_needed - food_in_kg)
    print(f"{food_needed} more kilos of food are needed.")
