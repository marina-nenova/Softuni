n = int(input())
lucky_numbers = ''

for x in range(1, 10):
    first_sum = 0
    second_sum = 0
    for y in range(1, 10):
        first_sum = x + y
        for z in range(1, 10):
            for i in range(1, 10):
                second_sum = z + i
                if first_sum == second_sum and n % first_sum == 0:
                    lucky_numbers += f"{x}{y}{z}{i} "
print(lucky_numbers)
