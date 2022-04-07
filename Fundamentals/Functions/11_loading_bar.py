def loading_bar_generator(num):
    loading_completed_index = num // 10
    loading_bar_list = []
    for ind in range(10):
        if ind < loading_completed_index:
            loading_bar_list.append("%")
        else:
            loading_bar_list.append(".")
    return "".join(loading_bar_list)


number = int(input())
loading_bar = loading_bar_generator(number)

if number == 100:
    print(f"{number}% Complete!")
    print(f"[{loading_bar}]")
else:
    print(f"{number}% [{loading_bar}]")
    print("Still loading...")
