def numbers_searching(*args):
    output = []

    lowest = min(args)
    highest = max(args)
    for num in range(lowest, highest + 1):
        if num not in args:
            output.append(num)

    duplicates = set(num for num in args if args.count(num) > 1)
    output.append(list(sorted(duplicates)))

    return output



print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))