class Pieces:

    def __init__(self, name, composer, key):
        self.name = name
        self.composer = composer
        self.key = key


n = int(input())
pieces = {}
for _ in range(n):
    piece, composer, key = input().split('|')
    pieces[piece] = Pieces(piece, composer, key)

command = input()

while not command == "Stop":
    data = command.split('|')
    action = data[0]
    piece = data[1]

    if action == "Add":
        composer = data[2]
        key = data[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            pieces[piece] = Pieces(piece, composer, key)
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif action == "Remove":
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces.pop(piece)
            print(f"Successfully removed {piece}!")

    elif action == "ChangeKey":
        new_key = data[2]
        if piece not in pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            pieces[piece].key = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    command = input()

for piece, info in pieces.items():
    print(f"{piece} -> Composer: {info.composer}, Key: {info.key}")
