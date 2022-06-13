import json

USERS_FILE_PATH = "./db/users.txt"
def register(username, email, password):
    user_obj = {"username": username,
                "email": email,
                "password": password

    }
    user_json = json.dumps(user_obj)

    with open(USERS_FILE_PATH, "r+") as file:
        for user_info in file:
            existing_user = json.loads(user_info.strip())
            if existing_user["username"] == username:
                return False
        file.write(user_json + "\n")
        return True

def login(username, password):
    with open(USERS_FILE_PATH, "r") as file:
        for user_info in file:
            existing_user = json.loads(user_info.strip())
            if existing_user["username"] == username and existing_user["password"] == password:
                return True
        return False


