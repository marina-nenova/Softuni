import json

def register(username, email, password):
    user_obj = {"username": username,
                "email": email,
                "password": password

    }
    user_json = json.dumps(user_obj)

    with open("./db/users.txt", "a") as file:
        file.write(user_json + "\n")



