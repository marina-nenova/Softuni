def list_manipulator(numbers, action, side, *args):

    if action == "add" and side == "beginning":
        numbers[0:0] = list(args)
    elif action == "add" and side == "end":
        numbers.extend(args)

    elif action == "remove":
        count = args[0] if args else 1
        for _ in range(count):
            if side == "beginning":
                numbers.pop(0)
            elif side == "end":
                numbers.pop()

    return numbers



print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
