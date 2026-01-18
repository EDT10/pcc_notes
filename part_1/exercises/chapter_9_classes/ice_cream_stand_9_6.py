"""
An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand 
that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 166). 
Either version of the class will work; just pick the one you like better. 
Add an attribute called flavors that stores a list of ice cream flavors. 
Write a method that displays theese flavors. Create an instance of IceCreamStand, and call this method.
"""

class Restaurant:
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Describing the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"{self.restaurant_name} specializes in {self.cousine_type} cousine.")

    def open_restaurant(self):
        """Simulating opening a restaurant"""
        print(f"{self.restaurant_name} is now OPEN!\n")

    def set_number_served(self, customers_served):
        """Updates the number of customers served by the given value."""
        self.number_served = customers_served
        print(f"The restaurant has served {self.number_served} customers.")

    def increment_number_served(self, served):
        "Increments number of customers served by the given number."
        self.number_served += served

class IceCreamStand(Restaurant):
    """Creating a specific kind of restaurant"""
    def __init__(self, restaurant_name, cousine_type):
        super().__init__(restaurant_name, cousine_type)
        # self.flavor = ["chocolate", "strawberry", "vanilla"]

        # better solution: create an empty list so that any ice cream stand can 
        # add their respective flavors to the list.
        self.flavor = []

    def display_flavors(self):
        """Shows all the flavors of ice cream served"""
        for flavor in self.flavor:
            print(f"We have {flavor.upper()} flavor available.")

chico_ice_truck = IceCreamStand("Chico Ice Truck", "Ice Cream")

chico_ice_truck.describe_restaurant()
chico_ice_truck.flavor = ["chocolate", "strawberry", "vanilla"]
chico_ice_truck.display_flavors()