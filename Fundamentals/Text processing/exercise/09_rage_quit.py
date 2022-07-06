string = input()
rage_message = ""
string_to_be_repeated = ""
num = ""
for index in range(len(string)):
    if not string[index].isdigit():
        string_to_be_repeated += string[index].upper()

    if string[index].isdigit():
        num += string[index]
        if index != len(string) - 1 and string[index + 1].isdigit():
            num += string[index + 1]

        rage_message += string_to_be_repeated * int(num)
        string_to_be_repeated = ""
        num = ""

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)
