class Restaurant():
    def __init__(self, name, cuisine_type):
        self.name = name.title()
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        msg = f"{self.name}: {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        msg = f"{self.name} est ouvert."
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        self.number_served += additional_served


restaurant = Restaurant('L\'Abbaye', 'Italien')
restaurant.describe_restaurant()

print(f"\nNumero servi: {restaurant.number_served}")
restaurant.number_served = 1
print(f"Numero servi: {restaurant.number_served}")

restaurant.set_number_served(2)
print(f"Numero servi: {restaurant.number_served}")

restaurant.increment_number_served(3)
print(f"Numero servi: {restaurant.number_served}")