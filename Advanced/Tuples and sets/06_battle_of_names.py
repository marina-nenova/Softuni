n = int(input())
even_sums = set()
odd_sums = set()

for row in range(1, n + 1):
    name = input()
    sum_chars = sum([ord(ch) for ch in name])
    devised_sum = sum_chars // row
    if devised_sum % 2 == 0:
        even_sums.add(devised_sum)
    else:
        odd_sums.add(devised_sum)

if sum(even_sums) == sum(odd_sums):
    union = even_sums.union(odd_sums)
    print(*union, sep=", ")

elif sum(odd_sums) > sum(even_sums):
    diff = odd_sums.difference(even_sums)
    print(*diff, sep=", ")

elif sum(even_sums) > sum(odd_sums):
    symmetric_diff = even_sums.symmetric_difference(odd_sums)
    print(*symmetric_diff, sep=", ")
