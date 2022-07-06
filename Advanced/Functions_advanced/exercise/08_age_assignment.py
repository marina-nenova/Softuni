def age_assignment(*args, **kwargs):
    output = ""
    assignment_dict = {}
    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        assignment_dict[name] = age

    for name, age in sorted(assignment_dict.items(), key=lambda kvpt: kvpt[0]):
        output += f"{name} is {age} years old.\n"
    return output



print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))