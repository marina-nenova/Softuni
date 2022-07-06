def grocery_store(**kwargs):
    result = ""
    sorted_dict = sorted(kwargs.items(),key= lambda kvpt: (-kvpt[1], -len(kvpt[0]), kvpt[0]))
    for product, quantity in sorted_dict:
        result += f"{product}: {quantity}\n"
    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
