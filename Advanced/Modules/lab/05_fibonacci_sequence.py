def create_fibonacci_sequence(number):
    fib = [0, 1]

    for _ in range(3, number + 1):
        fib.append(fib[-1] + fib[-2])
    return fib


command = input()
sequence = []

while not command == "Stop":
    data = command.split()
    action = data[0]
    if action == "Create":
        number = int(data[-1])
        sequence = create_fibonacci_sequence(number)
        print(*sequence, sep=" ")
    elif action == "Locate":
        number = int(data[1])
        if number not in sequence:
            print(f"The number {number} is not in the sequence")
        else:
            print(f"The number - {number} is at index {sequence.index(number)}")
    command = input()
