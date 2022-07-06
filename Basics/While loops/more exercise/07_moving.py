free_space_width = int(input())
free_space_lenght = int(input())
free_space_hight = int(input())
free_cubic_meters = free_space_width * free_space_lenght * free_space_hight


while free_cubic_meters > 0:
    number_of_boxes = input()
    if number_of_boxes == "Done":
        print(f"{free_cubic_meters} Cubic meters left.")
        break
    else:
        free_cubic_meters -= int(number_of_boxes)

if free_cubic_meters < 0:
    print(f"No more free space! You need {abs(free_cubic_meters)} Cubic meters more.")
