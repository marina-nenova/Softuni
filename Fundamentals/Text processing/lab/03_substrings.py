substring = input()
string = input()

while substring in string:
    string = string.replace(substring, "")

print(string)
