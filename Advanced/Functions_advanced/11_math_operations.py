from collections import deque


def math_operations(*args, **kwargs):
    numbers = deque(args)

    while numbers:
        for index in range(1, 5):
            current_number = numbers.popleft()
            if index == 1:
                kwargs['a'] += current_number
            elif index == 2:
                kwargs['s'] -= current_number
            elif index == 3 and current_number > 0:
                kwargs['d'] /= current_number
            elif index == 4:
                kwargs['m'] *= current_number
            if not numbers:
                break

    output = ""
    for key, value in sorted(kwargs.items(), key=lambda kvp: (-kvp[1], kvp[0])):
        output += f"{key}: {value:.1f}\n"

    return output



print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))

print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))

print(math_operations(6.0, a=0, s=0, d=5, m=0))