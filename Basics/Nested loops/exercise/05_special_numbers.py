number = int(input())

for num in range(1111, 10000):
    num_str = str(num)
    counter = 0
    for index, digit in enumerate(num_str):
        if int(digit) == 0:
            continue
        else:
            if number % int(digit) == 0:
                counter += 1
    if counter == 4:
        print(num, end=" ")