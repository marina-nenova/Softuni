n = int(input())
sum = 0

for num in range(n):
    number = int(input())
    sum += number
result = sum / n
print(f"{result:.2f}")