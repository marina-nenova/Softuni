def even_odd_sum(digits_list):
    evens = 0
    odds = 0
    for num in digits_list:
        if num % 2 == 0:
            evens += num
        else:
            odds += num
    return evens, odds


number = list(input())

digits_as_ints = [int(digit) for digit in number]

even_sum, odd_sum = even_odd_sum(digits_as_ints)
print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
