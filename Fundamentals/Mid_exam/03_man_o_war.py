def index_is_valid(index, ship):
    if 0 <= index < len(ship):
        return True
    else:
        return False


pirate_ship = list(map(int, input().split(">")))
warship = [int(el) for el in input().split(">")]
max_health_capacity = int(input())
need_repair_value = max_health_capacity * 0.2

command = input()
stalemate = True
while not command == "Retire":
    data = command.split()
    action = data[0]
    if action == "Fire":
        index = int(data[1])
        damage = int(data[2])
        if index_is_valid(index, warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                stalemate = False
                break

    elif action == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        if index_is_valid(start_index, pirate_ship) and index_is_valid(end_index, pirate_ship):
            sections = [el - damage for el in pirate_ship[start_index: end_index + 1]]
            pirate_ship[start_index : end_index + 1] = sections
            if len([sec for sec in pirate_ship if sec <= 0]) > 0:
                print("You lost! The pirate ship has sunken.")
                stalemate = False
                break

    elif action == "Repair":
        index = int(data[1])
        health = int(data[2])
        if index_is_valid(index, pirate_ship):
            pirate_ship[index] += health
            if pirate_ship[index] > max_health_capacity:
                pirate_ship[index] = max_health_capacity

    elif action == "Status":
        needs_repair_count = len([sec for sec in pirate_ship if sec < need_repair_value])
        print(f"{needs_repair_count} sections need repair.")
    command = input()

if stalemate:
    pirate_ship_status = sum(pirate_ship)
    warship_status = sum(warship)
    print(f"Pirate ship status: {pirate_ship_status}")
    print(f"Warship status: {warship_status}")