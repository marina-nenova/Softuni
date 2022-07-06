target_hight = int(input())
starting_hight = target_hight - 30
tries = 0
has_failed = False
failed_hight = 0
for hight in range(starting_hight, target_hight + 1, 5):
    fail_counter = 0
    for attempts in range(3):
        attempt = int(input())
        tries +=1
        if attempt > hight:
            break
        else:
            fail_counter += 1
            if fail_counter == 3:
                has_failed = True
                failed_hight = hight
                break
    if has_failed:
        break
if has_failed:
    print(f"Tihomir failed at {failed_hight}cm after {tries} jumps.")
else:
    print(f"Tihomir succeeded, he jumped over {target_hight}cm after {tries} jumps.")



