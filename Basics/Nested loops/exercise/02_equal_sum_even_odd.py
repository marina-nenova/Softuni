first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    even_sum = 0
    odd_sum = 0
    current_number_str = str(current_number)
    for index, digit in enumerate(current_number_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if odd_sum == even_sum:
        print(current_number, end=" ")