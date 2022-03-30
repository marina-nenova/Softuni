n = int(input())

for num in range(1, n + 1):
    string_num = str(num)
    sum_digit = 0
    for digit in string_num:
        sum_digit += int(digit)
    if (sum_digit == 5) or (sum_digit == 7) or (sum_digit) == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")

A=[]
for I in range(10):
    A.append(I)
    for A[I] in A:
        print(A[I])