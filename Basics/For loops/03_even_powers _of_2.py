n = int(input())

for num in range(0, n + 1): #(0, n + 1, 2)
    if num % 2 == 0:
        total = 2 ** num
        print(total)
