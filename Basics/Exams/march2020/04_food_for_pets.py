

number_of_days = int(input())
total_food_quantity = float(input())
total_eaten_bisquits = 0
total_food_eaten = 0
dog_food_eaten = 0
cat_food_eaten = 0

for day in range(1, number_of_days + 1):
    dog_daily_consumption = int(input())
    cat_daily_consumption = int(input())
    if day % 3 == 0:
        total_eaten_bisquits += (dog_daily_consumption + cat_daily_consumption) * 0.1
    dog_food_eaten += dog_daily_consumption
    cat_food_eaten += cat_daily_consumption
    total_food_eaten += dog_daily_consumption + cat_daily_consumption
total_food_eaten_percentage = (total_food_eaten / total_food_quantity) * 100
dog_food_eaten_percentage = (dog_food_eaten / total_food_eaten) * 100
cat_food_eaten_percentage = (cat_food_eaten / total_food_eaten) * 100
print(f"Total eaten biscuits: {round(total_eaten_bisquits)}gr.")
print(f"{total_food_eaten_percentage:.2f}% of the food has been eaten.")
print(f"{dog_food_eaten_percentage:.2f}% eaten from the dog.")
print(f"{cat_food_eaten_percentage:.2f}% eaten from the cat.")
