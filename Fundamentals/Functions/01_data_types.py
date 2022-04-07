def data_types_manipulator(data_type, variable):
    if data_type == "int":
        return int(variable) * 2
    elif data_type == "real":
        result = float(variable) * 1.5
        return f"{result:.2f}"
    elif data_type == "string":
        return f"${variable}$"


type_of_variable = input()
text = input()
print(data_types_manipulator(type_of_variable, text))
