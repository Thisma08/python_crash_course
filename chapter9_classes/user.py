class User():
    def __init__(self, first_name, last_name, username, email, location):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Username: {self.username}")
        print(f"  Email: {self.email}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        print(f"\nBienvenue, {self.username}!")

u1 = User('mathis', 'mahaux', 'thisma08', 'mathis@up-db.com', 'belgique')
u1.describe_user()
u1.greet_user()

u2 = User('alice', 'musette', 'arisu', 'alice@up-db.com', 'belgique')
u2.describe_user()
u2.greet_user()