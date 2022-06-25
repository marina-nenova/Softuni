def flights(*args):
    flights_dict = {}
    for index in range(0, len(args), 2):
        destination = args[index]

        if destination == "Finish":
            break

        passengers = args[index + 1]

        if destination not in flights_dict:
            flights_dict[destination] = 0
        flights_dict[destination] += int(passengers)
    return flights_dict



print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))

print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))

print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))