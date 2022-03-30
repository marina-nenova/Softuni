n = int(input())
unbalanced = False
last_symbol = ""
for i in range(n):
    symbol = input()
    if symbol not in "), (":
        continue
    if last_symbol == "" and symbol == ")" or last_symbol == symbol:
        unbalanced = True
        break
    last_symbol = symbol
if unbalanced:
    print("UNBALANCED")
else:
    print("BALANCED")