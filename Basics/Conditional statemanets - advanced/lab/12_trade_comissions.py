city = input()
volume = float(input())
comissions = 0
condition = True
if city == "Sofia":
    if 0 <= volume <= 500:
        comission = volume * 0.05
    elif 500 <= volume <= 1000:
        comission = volume * 0.07
    elif 1000 <= volume <= 10000:
        comission = volume * 0.08
    elif volume > 10000:
        comission = volume * 0.12
    else:
        condition = False

elif city == "Varna":
    if 0 <= volume <= 500:
        comission = volume * 0.045
    elif 500 <= volume <= 1000:
        comission = volume * 0.075
    elif 1000 <= volume <= 10000:
        comission = volume * 0.1
    elif volume > 10000:
        comission = volume * 0.13
    else:
        condition = False
elif city == "Plovdiv":
    if 0 <= volume <= 500:
        comission = volume * 0.055
    elif 500 <= volume <= 1000:
        comission = volume * 0.08
    elif 1000 <= volume <= 10000:
        comission = volume * 0.12
    elif volume > 10000:
        comission = volume * 0.145
    else:
        condition = False
else:
    condition = False

if condition:
    print(f"{comission:.2f}")
else:
    print("error")