numbers = [int(el) for el in input().split(", ")]

group = 10

while len(numbers) > 0:
    list_of_numbers = [num for num in numbers if num <= group]
    print(f"Group of {group}'s: {list_of_numbers}")
    numbers = [num for num in numbers if num > group]
    group += 10
