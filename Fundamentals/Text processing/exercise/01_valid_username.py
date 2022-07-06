# usernames = input().split(", ")
#
# for name in usernames:
#     if 3 <= len(name) <= 16 and name.isalnum() or "-" in name or "_" in name:
#         print(name)
import re

usernames = input().split(", ")
pattern = r"^[A-Za-z0-9_-]*$"

for name in usernames:
    if re.match(pattern, name) and 3 <= len(name) <= 16:
        print(name)