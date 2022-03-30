number = input()
number_list = []
largest_number = ""

for digit in number:
    number_list.append(int(digit))

number_list.sort(reverse=True)

print(*number_list, sep="")