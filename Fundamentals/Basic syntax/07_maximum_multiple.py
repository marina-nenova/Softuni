divisor = int(input())
boundary = int(input())
largest = 0
for i in range(1, boundary + 1):
    if i % divisor == 0 and i > largest:
        largest = i
print(largest)