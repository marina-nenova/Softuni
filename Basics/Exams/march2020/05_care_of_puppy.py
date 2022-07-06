food_bought_in_kg = int(input())
food_bought_in_gr = food_bought_in_kg * 1000
total_grams_eaten = 0
command = input()

while command != "Adopted":
    food_per_day = int(command)
    total_grams_eaten += food_per_day
    command = input()
difference = abs(food_bought_in_gr - total_grams_eaten)
if total_grams_eaten <= food_bought_in_gr:
    print(f"Food is enough! Leftovers: {difference} grams.")
else:
    print(f"Food is not enough. You need {difference} grams more." )
