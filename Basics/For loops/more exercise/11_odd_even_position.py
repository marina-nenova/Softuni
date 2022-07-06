import sys

n = int(input())
even_sum = 0
odd_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize
odd_min = sys.maxsize
odd_max = -sys.maxsize

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        even_sum += num
        if num < even_min:
            even_min = num
        if num > even_max:
            even_max = num
    elif i % 2 != 0:
        odd_sum += num
        if num < odd_min:
            odd_min = num
        if num > odd_max:
            odd_max = num

if n == 0:
    print(f"OddSum={odd_sum:.2f},")
    print("OddMin=No,")
    print("OddMax=No,")
    print(f"EvenSum={even_sum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")
elif n == 1:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},")
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
    print(f"EvenSum={even_sum:.2f},")
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
