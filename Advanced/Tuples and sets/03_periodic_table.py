n = int(input())
unique_elements = set()

for _ in range(n):
    data = input().split()
    while data:
        unique_elements.add(data.pop())

print(*unique_elements, sep="\n")
