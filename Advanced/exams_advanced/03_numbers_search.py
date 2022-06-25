def numbers_searching(*args):
    min_num = min(args)
    max_num = max(args)

    result = []
    duplicates = []
    for num in range(min_num, max_num + 1):
        if num not in args:
            result.append(num)
        if args.count(num) > 1:
            duplicates.append(num)

    result.append(duplicates)

    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))