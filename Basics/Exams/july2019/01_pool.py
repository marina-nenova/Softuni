import math

number_of_people = int(input())
entry_fee = float(input())
price_per_lounger = float(input())
price_per_umbrella = float(input())

total_entry_fee = number_of_people * entry_fee
loungers = math.ceil(number_of_people * 0.75)
umbrellas = math.ceil(number_of_people * 0.5)

total_price_per_loungers = price_per_lounger * loungers
total_price_per_umbrellas = price_per_umbrella * umbrellas

total_sum = total_entry_fee + total_price_per_loungers + total_price_per_umbrellas
print(f"{total_sum:.2f} lv.")