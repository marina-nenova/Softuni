voucher = int(input())
tickets_bought = 0
other_expences = 0
command = input()
value = 0
while command != "End":
    if len(command) > 8:
        value = ord(command[0]) + ord(command[1])
        if value <= voucher:
            tickets_bought +=1
    else:
        value = ord(command[0])
        if value <= voucher:
            other_expences += 1
    voucher -= value
    if voucher < 0:
        break
    command = input()
print(tickets_bought)
print(other_expences)