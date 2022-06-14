import json

from auth_service import get_current_user
PRODUCTS_FILE_PATH = "./db/products.txt"

def get_all_products():
    with open(PRODUCTS_FILE_PATH, "r") as file:
        return [json.loads(el.strip()) for el in file]


def buy_product(product_id):
    with open(PRODUCTS_FILE_PATH, "r+") as products_file:
        result = []
        for product_line in products_file:
            current_product = json.loads(product_line.strip())
            if current_product['id'] == product_id:
                current_product['count'] -= 1
                result.append(json.dumps(current_product) + "\n")
            else:
                result.append(product_line)

        products_file.seek(0)
        products_file.truncate()

        products_file.writelines(result)
