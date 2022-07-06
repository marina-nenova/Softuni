numbers = input().split(", ")

for digit in numbers:
    if digit == "0":
        numbers.remove("0")
        numbers.append("0")

numbers_as_ints = [int(str) for str in numbers]

print(numbers_as_ints)
