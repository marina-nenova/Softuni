import sys

n = int(input())
current_sum = 0
previous_sum = 0
diff = 0
max_diff = -sys.maxsize

for i in range(n):
    number1 = int(input())
    number2 = int(input())
    if i != 0:
        previous_sum = current_sum
        current_sum = number1 + number2
        diff = abs(current_sum - previous_sum)
        if diff > max_diff:
            max_diff = diff
    else:
        current_sum = number1 + number2
if diff == 0 or n == 1:
    print(f"Yes, value={current_sum}")
else:
    print(f"No, maxdiff={max_diff}")
