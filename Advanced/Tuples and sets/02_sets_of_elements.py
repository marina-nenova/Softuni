n, m = [int(el) for el in input().split()]
set1 = set()
set2 = set()

for count in range(n + m):
    number = int(input())
    if count < n:
        set1.add(number)
    else:
        set2.add(number)

common_elements = set1.intersection(set2)

print(*common_elements, sep="\n")
