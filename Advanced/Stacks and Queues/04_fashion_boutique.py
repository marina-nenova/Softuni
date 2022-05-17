box_of_clothes = [int(el) for el in input().split()]
rack_capacity = int(input())

racks_count = 0
while box_of_clothes:
    current_rack = 0
    while box_of_clothes and current_rack + box_of_clothes[-1] <= rack_capacity:
        current_rack += box_of_clothes.pop()
    racks_count += 1

print(racks_count)


# box_of_clothes = [int(el) for el in input().split()]
# rack_capacity = int(input())
#
# used_racks = 1
# current_rack = rack_capacity
#
# while box_of_clothes:
#     current_piece = box_of_clothes[-1]
#     if current_piece <= current_rack:
#         box_of_clothes.pop()
#         current_rack -= current_piece
#     else:
#         used_racks += 1
#         current_rack = rack_capacity
#
# print(used_racks)