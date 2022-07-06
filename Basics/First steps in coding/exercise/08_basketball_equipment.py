annual_expences = int(input())

shoes = annual_expences - annual_expences * 0.4
clothes = shoes - shoes * 0.2
ball = clothes / 4
accessories = ball / 5

total_expences = annual_expences + shoes + clothes + ball + accessories
print(total_expences)