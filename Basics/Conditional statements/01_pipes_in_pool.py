v = int(input())
pipe1 = int(input())
pipe2 = int(input())
hours = float(input())

debit1 = pipe1 * hours
debit2 = pipe2 * hours

total_debit = debit1 + debit2
total_percent = (total_debit / v) * 100
debit1_percent = (debit1 / total_debit) * 100
debit2_percent = (debit2 / total_debit) * 100

if total_debit <= v:
    print(f"The pool is {total_percent:.2f}% full. Pipe 1: {debit1_percent:.2f}%. Pipe 2: {debit2_percent:.2f}%.")
else:
    overflow = total_debit - v
    print(f"For {hours} hours the pool overflows with {overflow:.2f} liters.")