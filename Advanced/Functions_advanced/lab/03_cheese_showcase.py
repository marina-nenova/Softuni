def sorting_cheeses(**kwargs):
    output = ""
    for cheese, quantities in sorted(kwargs.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0])):
        output += cheese + "\n"
        ordered_quantities = sorted(quantities, reverse=True)
        output += "\n".join([str(el) for el in ordered_quantities]) + '\n'

    return  output



print(
    sorting_cheeses(
        Parmigiano=[165, 215],
        Feta=[150, 515],
        Brie=[150, 125]
    )
)
