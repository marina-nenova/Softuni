def even_odd_filter(**kwargs):
    num_dict = {}
    for type, nums in kwargs.items():
        if type == "odd":
            nums = [num for num in nums if num % 2 != 0]
        elif type == "even":
            nums = [num for num in nums if num % 2 == 0]
        num_dict[type] = nums
    sorted_dict = dict(sorted(num_dict.items(), key= lambda kvpt: -len(kvpt[1])))
    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
