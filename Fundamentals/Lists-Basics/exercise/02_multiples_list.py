factor = int(input())
count = int(input())
multiples_list = []
previous_number = factor
for num in range(count):
    multiples_list.append(previous_number)
    current_number = previous_number + factor
    previous_number = current_number

print(multiples_list)