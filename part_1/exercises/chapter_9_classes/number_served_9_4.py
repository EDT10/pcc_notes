"""
Start with your program from Exercise 9-1 (page 162). Add an attribute called 
number_served with a default value of 0. Create an instance called restaurant from this class. 
Print the number of customers the restaurant has served, and then change this value and print it again.

Add a method called set_number_served() that lets you set the number of customers 
that have been served. Call this method with a new number and print the value again.

Add a method called increment_number_served() that lets you increment the number 
of customers who've been served. Call this method with any number you like that 
could represent how many customers were served in, say, a day of business.
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
        

# making an instance of the Restaurant Class
restaurant = Restaurant("Chutney", "Indian")

# calling both methods in the Restaurant class
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"Customers served: {restaurant.number_served}")
restaurant.number_served = 23
print(f"Customers served: {restaurant.number_served}\n")

restaurant.set_number_served(90)

restaurant.increment_number_served(90)
print(f"Customers served: {restaurant.number_served}\n")
