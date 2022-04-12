number_of_rooms = int(input())
free_chairs = 0
for room in range(1, number_of_rooms + 1):
    chairs, visitors = input().split()
    difference = abs(len(chairs) - int(visitors))
    if len(chairs) < int(visitors):
        print(f"{difference} more chairs needed in room {room}")
        free_chairs -= difference
    else:
        free_chairs += difference

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")
