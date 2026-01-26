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