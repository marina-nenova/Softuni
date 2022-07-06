minutes_walking = int(input())
number_of_walks = int(input())
calories_eaten = int(input())

total_minutes_walking = number_of_walks * minutes_walking
calories_burnt = total_minutes_walking * 5
burnt_calories_needed = calories_eaten * 0.5

if calories_burnt >= burnt_calories_needed:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories_burnt}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories_burnt}.")