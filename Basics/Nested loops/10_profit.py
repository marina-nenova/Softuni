number_of_1 = int(input())
number_of_2 = int(input())
number_of_5 = int(input())
sum = int(input())

for coins1 in range(0, number_of_1 +1):
    for coins2 in range(0, number_of_2 + 1):
        for coins5 in range(0, number_of_5 + 1):
            if (coins1 * 1) + (coins2 * 2) + (coins5 * 5) == sum:
                print(f"{coins1} * 1 lv. + {coins2} * 2 lv. + {coins5} * 5 lv. = {sum} lv.")
