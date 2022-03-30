number_of_snowballs = int(input())
best_snowball_value = 0
best_weight = 0
best_time_to_target = 0
best_quality = 0
for snowball in range(number_of_snowballs):
    weight = int(input())
    time_to_target = int(input())
    quality = int(input())
    snowball_value = (weight / time_to_target) ** quality
    if snowball_value > best_snowball_value:
        best_snowball_value = snowball_value
        best_time_to_target = time_to_target
        best_weight = weight
        best_quality = quality

print(f"{best_weight} : {best_time_to_target} = {int(best_snowball_value)} ({best_quality})")