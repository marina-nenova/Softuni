def sum_nums(nums):
    result = 0
    for num in nums:
        result += num
    return result


numbers = [int(el) for el in input().split()]
positives = [el for el in numbers if el > 0]
negatives = [el for el in numbers if el < 0]

negatives_sum = sum_nums(negatives)
positives_sum = sum_nums(positives)

print(negatives_sum)
print(positives_sum)

if abs(negatives_sum) > positives_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
