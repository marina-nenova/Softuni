import re

n = int(input())
pattern = r"(^|(?<=\s))([$|%])(?P<tag>[A-Z][a-z]{2,})\1: (?P<message>\[\d+\]\|\[\d+\]\|\[\d+\]\|)($|(?=\s))"
for _ in range(n):
    encrypted_message = input()
    matches = re.search(pattern, encrypted_message)
    tag = ""
    message = ""
    if matches:
        tag = matches.group('tag')
        message += [chr(int(num)) for num in matches.group('message').split('|')]
        print(f"{tag}: {message}")
    else:
        print("Valid message not found!")