def index_is_valid(index):
    if 0 <= index < len(stops):
        return True
    return False


stops = input()

command = input()

while not command == "Travel":
    data = command.split(":")
    action = data[0]
    if action == "Add Stop":
        index = int(data[1])
        stop = data[2]
        if index_is_valid(index):
            stops = stops[:index] + stop + stops[index:]

    elif action == "Remove Stop":
        start_index = int(data[1])
        end_index = int(data[2])
        if index_is_valid(start_index) and index_is_valid(end_index):
            to_be_removed = stops[start_index:end_index + 1]
            stops = stops.replace(to_be_removed, "")

    elif action == "Switch":
        old_stop = data[1]
        new_stop = data[2]
        stops = stops.replace(old_stop, new_stop)

    print(stops)
    command = input()

print(f"Ready for world tour! Planned stops: {stops}")
