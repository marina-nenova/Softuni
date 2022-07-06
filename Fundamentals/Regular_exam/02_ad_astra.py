import math
import re

text = input()
cal_needed_per_day = 2000
pattern = r"(?P<separator>[#|\|])(?P<item>[A-Za-z\s]+)(?P=separator)(?P<date>\d{2}/\d{2}/\d{2})(?P=separator)(?P<calories>[0-9][0-9]{0,3}|10000)(?P=separator)"

food_items = list(re.finditer(pattern, text))

total_calories = sum([int(item.group("calories")) for item in food_items])
days = total_calories // cal_needed_per_day
print(f"You have food to last you for: {days} days!")

for item in food_items:
    print(f"Item: {item.group('item')}, Best before: {item.group('date')}, Nutrition: {item.group('calories')}")
