viewing = input()
rows = int(input())
columns = int(input())

income = 0
cinema_capacity = rows * columns
if viewing == "Premiere":
    income = cinema_capacity * 12
elif viewing == "Normal":
    income = cinema_capacity * 7.5
elif viewing == "Discount":
    income = cinema_capacity * 5

print(f"{income:.2f} leva")
