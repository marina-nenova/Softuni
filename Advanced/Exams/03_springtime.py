def start_spring(**kwargs):
    spring_objects = {}

    for spring_object, object_type in kwargs.items():
        if object_type not in spring_objects:
            spring_objects[object_type] = []
        spring_objects[object_type].append(spring_object)

    sorted_spring_objects = sorted(spring_objects.items(), key=lambda kvpt: (-len(kvpt[1]), kvpt[0]))

    output = ""

    for object_type, objects in sorted_spring_objects:
        output += f"{object_type}:\n"
        for spring_object in sorted(objects):
            output += f"-{spring_object}\n"

    return output


# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))
#
#
# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
