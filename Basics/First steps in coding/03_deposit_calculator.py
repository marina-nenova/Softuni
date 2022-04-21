deposited = float(input())
time = int(input())
interest = float(input())

sum = deposited + time * ((deposited * (interest / 100) / 12))
print(sum)