import re
pattern = r"\d+"
line = input()
while True:
    if line:
        match = re.findall(pattern, line)
        if match:
            print(" ".join(match), end=" ")
        line = input()
    else:
        break
