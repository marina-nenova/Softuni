number_of_rounds = int(input())
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
invalid_numbers = 0
total_points = 0

for round in range(number_of_rounds):
    number = int(input())
    if 0 <= number <= 9:
        from_0_to_9 +=1
        total_points += number * 0.2
    elif 10 <= number <= 19:
        from_10_to_19 += 1
        total_points += number * 0.3
    elif 20 <= number <= 29:
        from_20_to_29 += 1
        total_points += number * 0.4
    elif 30 <= number <= 39:
        from_30_to_39 += 1
        total_points += 50
    elif 40 <= number <= 50:
        from_40_to_50 += 1
        total_points += 100
    else:
        invalid_numbers +=1
        total_points /= 2

from_0_to_9_percent = (from_0_to_9 / number_of_rounds) * 100
from_10_to_19_percent = (from_10_to_19 / number_of_rounds) * 100
from_20_to_29_percent = (from_20_to_29 / number_of_rounds) * 100
from_30_to_39_percent = (from_30_to_39 / number_of_rounds) * 100
from_40_to_50_percent = (from_40_to_50 / number_of_rounds) * 100
invalid_numbers_percent = (invalid_numbers / number_of_rounds) * 100

print(f"{total_points:.2f}")
print(f"From 0 to 9: {from_0_to_9_percent:.2f}%")
print(f"From 10 to 19: {from_10_to_19_percent:.2f}%")
print(f"From 20 to 29: {from_20_to_29_percent:.2f}%")
print(f"From 30 to 39: {from_30_to_39_percent:.2f}%")
print(f"From 40 to 50: {from_40_to_50_percent:.2f}%")
print(f"Invalid numbers: {invalid_numbers_percent:.2f}%")
