last_sector = input()
rows_in_first_sector = int(input())
num_of_seats_in_odd_rows = int(input())
counter = 0
sector_as_num = ord(last_sector)
for sector in range(ord("A"), sector_as_num + 1):
    sect = chr(sector)
    rows_in_first_sector = rows_in_first_sector + 1
    for rows in range(1, rows_in_first_sector):
        if rows % 2 == 1:
            for seat in range(ord("a"), ord("a") + num_of_seats_in_odd_rows):
                print(f"{sect}{rows}{chr(seat)}")
                counter += 1
        else:
            for seat in range(ord("a"), ord("a") + num_of_seats_in_odd_rows + 2):
                print(f"{sect}{rows}{chr(seat)}")
                counter += 1

print(counter)