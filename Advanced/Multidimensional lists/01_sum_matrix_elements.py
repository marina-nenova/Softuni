rows, cols = [int(el) for el in input().split(", ")]

matrix = []
result = 0
for _ in range(rows):
    line = [int(el) for el in input().split(", ")]
    matrix.append(line)
    result += sum(line)

print(result)
print(matrix)