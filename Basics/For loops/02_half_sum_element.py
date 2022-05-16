import sys

n = int(input())
sum = 0
max_num = -sys.maxsize
for i in range(n):
    num = int(input())
    sum += num
    if num > max_num:
        max_num = num
sum_others = sum - max_num
if max_num == sum_others:
    print("Yes")
    print(f"Sum = {sum_others}")
else:
    print("No")
    diff = abs(max_num - sum_others)
    print(f"Diff = {diff}")