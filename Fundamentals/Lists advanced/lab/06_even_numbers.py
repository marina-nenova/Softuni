numbers = [int(el) for el in input().split(", ")]
even_numbers_indices = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
even_numbers_indices1 = [index for index, value in enumerate(numbers) if value % 2 == 0]
print(even_numbers_indices)
print(even_numbers_indices1)

