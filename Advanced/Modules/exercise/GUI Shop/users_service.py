import json

from auth_service import get_current_user


def purchase_product(product_id):
    current_username = get_current_user()

    with open("./db/users.txt", "r+") as file:
        result = []
        for user_line in file:
            user_obj = json.loads(user_line.strip())
            if user_obj['username'] == current_username:
                user_obj['products'].append(product_id)
                result.append(json.dumps(user_obj) + '\n')
            else:
                result.append(user_line)

        file.seek(0)
        file.truncate()

        file.writelines(result)
