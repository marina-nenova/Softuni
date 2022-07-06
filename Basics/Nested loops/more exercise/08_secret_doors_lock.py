first_number = int(input())
second_number = int(input())
third_number = int(input())
number_is_prime = False
for digit1 in range(2, first_number + 1, 2):
    for digit2 in range(2, second_number + 1):
        for digit3 in range(2, third_number + 1, 2):
            counter = 0
            for i in range(1, digit2 + 1):
                if digit2 % i == 0:
                    counter += 1
            if counter == 2:
                print(f"{digit1} {digit2} {digit3}")
