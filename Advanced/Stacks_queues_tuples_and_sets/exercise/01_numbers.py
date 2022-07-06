first_set = set(int(el) for el in input().split())
second_set = set(int(el) for el in input().split())
n = int(input())

for _ in range(n):
    data = input()
    if data == "Check Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")
    else:
        action = data.split()
        command = action[0]
        set_to_change = action[1]
        sequence = [int(el) for el in action[2:]]
        if command == "Add":
            if set_to_change == "First":
                [first_set.add(int(el)) for el in sequence]
            elif set_to_change == "Second":
                [second_set.add(int(el)) for el in sequence]
        elif command == "Remove":
            if set_to_change == "First":
                first_set = first_set.difference(sequence)
            elif set_to_change == "Second":
                second_set = second_set.difference(sequence)

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")
