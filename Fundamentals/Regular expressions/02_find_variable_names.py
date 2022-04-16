# import re
#
# text = input()
# pattern = r"(?<=\s_)[A-Za-z0-9]*($|(?=[\.\s]))"
#
# valid_names = re.finditer(pattern, text)
# valid_names = [name.group() for name in valid_names]
#
# print(*valid_names, sep=",")
#
# import re
# text = input()
# pattern = r"\b_([A-Za-z0-9]+)\b"
#
# matches = re.findall(pattern, text)
# print(*matches, sep=",")

import re

results = []
reg = r"(?<=[_]{1})([a-zA-Z0-9]+)(?=[\s])\b"
text = input()
results.extend(re.findall(reg, text))
print(",".join(results), end=" ")