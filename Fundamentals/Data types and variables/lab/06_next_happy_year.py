# current_year = int(input())
#
# while True:
#     current_year += 1
#     current_year_as_str = str(current_year)
#     if len(current_year_as_str) == len(set(current_year_as_str)):
#         print(current_year_as_str)
#         break

current_year = int(input())

while True:
    current_year += 1
    current_year_as_str = str(current_year)
    happy_year = True
    for test_position in range(len(current_year_as_str)):
        test_digit = current_year_as_str[test_position]
        for current_position in range(test_position +1, len(current_year_as_str)):
            if test_digit == current_year_as_str[current_position]:
                happy_year = False
                break
    if happy_year:
        print(current_year)
        break