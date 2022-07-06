def get_info(**kwargs):
    name = kwargs.get("name")
    town = kwargs.get("town")
    age = kwargs.get("age")
    return f"This is {name} from {town} and he is {age} years old"

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))