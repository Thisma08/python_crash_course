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


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type='creme glacee'):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def show_flavors(self):
        print("\nParfums dispo:")
        for flavor in self.flavors:
            print(f"- {flavor.title()}")


glacier = IceCreamStand('Glacier')
glacier.flavors = ['vanille', 'chocolat', 'pistache', 'fraise']
glacier.describe_restaurant()
glacier.show_flavors()