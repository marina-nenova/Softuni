# numbers = [float(num) for num in input().split()]
# absolutes_list = [abs(num)for num in numbers]
#
# print(absolutes_list)


def absolute_numbers(numbers_list):
    absolute_numbers_list = []
    for num in numbers_list:
        absolute_numbers_list.append(abs(num))
    return absolute_numbers_list


numbers = [float(num) for num in input().split()]
print(absolute_numbers(numbers))


