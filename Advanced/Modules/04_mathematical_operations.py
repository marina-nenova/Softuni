from simple_operations.helper import operation_mapper

data = input().split()

a = float(data[0])
sign = data[1]
b = float(data[2])

result = operation_mapper[sign](a, b)
print(f"{result:.2f}")