numbers_list = [int(el) for el in input().split()]
n = int(input())

for times in range(n):
    numbers_list.remove(min(numbers_list))

print(*numbers_list, sep=", ")
