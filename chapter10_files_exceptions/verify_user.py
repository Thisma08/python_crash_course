from pathlib import Path
import json

def get_stored_username(path):
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
    username = input("Votre nom? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        correct = input(f"Etes-vous {username}? (y/n) ")
        if correct == 'y':
            print(f"Bienvenue, {username}.")
        else:
            username = get_new_username(path)
    else:
        username = get_new_username(path)

greet_user()
