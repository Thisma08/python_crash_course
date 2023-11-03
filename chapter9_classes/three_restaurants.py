class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        msg = f"{self.name}: {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} est ouvert."
        print(f"\n{msg}")

r1 = Restaurant('L\'Abbaye', 'Italien')
r1.describe_restaurant()

r2 = Restaurant("La Chine", 'Chinois')
r2.describe_restaurant()

r3 = Restaurant('Le Manhattan', 'Americain')
r3.describe_restaurant()