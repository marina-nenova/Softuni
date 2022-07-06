def operate(sign, *args):
    result = str(args[0])
    for el in args[1:]:
        result += sign + str(el)

    return eval(result)


print(operate("*", 3, 4))
