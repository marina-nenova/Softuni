health = 100
bitcoins = 0

dungeon = input().split("|")
current_room = 0
you_died = False

for room in dungeon:
    data = room.split()
    command = data[0]
    value = int(data[1])
    current_room += 1
    if command == "potion":
        if health + value > 100:
            value = 100 - health
        health += value
        print(f"You healed for {value} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += value
        print(f"You found {value} bitcoins.")

    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            you_died = True
            print(f"You died! Killed by {command}." )
            print(f"Best room: {current_room}")
            break

if not you_died:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


