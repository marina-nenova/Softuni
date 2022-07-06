numbers = [float(el) for el in input().split()]

numbers_dict = {}

for num in numbers:
    if num not in numbers_dict:
        numbers_dict[num] = 0
    numbers_dict[num] += 1

for data in numbers_dict.items():
    print(f"{data[0]:.1f} - {data[1]} times")
