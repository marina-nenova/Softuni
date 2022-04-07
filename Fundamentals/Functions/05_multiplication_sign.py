number1 = int(input())
number2 = int(input())
number3 = int(input())

numbers_list = [number1, number2, number3]
numbers_list_negatives = list(filter(lambda x: x < 0, numbers_list))
if numbers_list.count(0) > 0:
    print("zero")
elif len(numbers_list_negatives) % 2 == 1:
    print("negative")
else:
    print("positive")
