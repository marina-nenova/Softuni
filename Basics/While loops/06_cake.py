width = int(input())
lenght = int(input())
cake_pieces = width * lenght

while cake_pieces > 0:
    pieces_taken = input()
    if pieces_taken == "STOP":
        print(f"{cake_pieces} pieces are left.")
        break
    cake_pieces -= int(pieces_taken)
if cake_pieces < 0:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
