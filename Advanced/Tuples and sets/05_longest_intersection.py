n = int(input())
set_1 = set()
set_2 = set()
longest_intersection = set()
longest_length = 0
for _ in range(n):
    first, second = input().split("-")
    first_start, first_end = [int(el) for el in first.split(",")]
    second_start, second_end = [int(el) for el in second.split(",")]

    for n in range(first_start, first_end + 1):
        set_1.add(n)

    for m in range(second_start, second_end + 1):
        set_2.add(m)

    intersection = set_1.intersection(set_2)

    if len(intersection) > longest_length:
        longest_length = len(intersection)
        longest_intersection = intersection
    set_1.clear()
    set_2.clear()

print(f"Longest intersection is [{', '.join([str(el) for el in sorted(longest_intersection)])}] with length {longest_length}")
