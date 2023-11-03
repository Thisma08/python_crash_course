class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nBienvenue, {self.username}!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user = User('mathis', 'mahaux', 'thisma08', 'mathis@up-db.com', 'belgique')
user.describe_user()
user.greet_user()

print("\n3 essais de login.")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"  Essais de login: {user.login_attempts}")

print("Reinitialisation des essais de login.")
user.reset_login_attempts()
print(f"  Essais de login: {user.login_attempts}")