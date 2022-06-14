import json


def get_all_products():
    with open("./db/products.txt", "r") as file:
        return [json.loads(el.strip()) for el in file]