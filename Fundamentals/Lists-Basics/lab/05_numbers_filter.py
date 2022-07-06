# n = int(input())
#
# evens = []
# odds = []
# negatives = []
# positives = []
#
# for _ in range(n):
#     number = int(input())
#     if number % 2 == 0:
#         evens.append(number)
#     if number % 2 == 1:
#         odds.append(number)
#     if number >= 0:
#         positives.append(number)
#     if number < 0:
#         negatives.append(number)
# command = input()
# if command == "even":
#     print(evens)
# elif command == "odd":
#     print(odds)
# elif command == "positive":
#     print(positives)
# else:
#     print(negatives)

n = int(input())
numbers_list = []

for i in range(n):
    number = int(input())
    numbers_list.append(number)

command = input()

if command == "even":
    print([num for num in numbers_list if num % 2 == 0])
elif command == "odd":
    print([num for num in numbers_list if num % 2 != 0])
elif command == "negative":
    print([num for num in numbers_list if num < 0])
elif command == "positive":
    print([num for num in numbers_list if num >= 0])
