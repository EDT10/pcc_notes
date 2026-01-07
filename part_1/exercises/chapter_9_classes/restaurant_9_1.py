"""
Make a class called Restaurant. The __init__() method for Restaurant should store 
two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() 
that prints these two pieces of information, and a method called open_restaurant() 
that prints a message indicating that the restaurant is open.

Make an instance called restaurant from your class. Print the two attributes 
individually, and then call both methods.
"""

class Restaurant:
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def describe_restaurant(self):
        """Describing the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name}.")
        print(f"{self.restaurant_name} specializes in {self.cousine_type} cousine.")

    def open_restaurant(self):
        """Simulating opening a restaurant"""
        print(f"{self.restaurant_name} is now OPEN!")

# making an instance of the Restaurant Class
restaurant = Restaurant("Chutney", "Indian")

#displaying the individual attributes of the restaurant
print(restaurant.restaurant_name)
print(restaurant.cousine_type)

# calling both methods in the Restaurant class
restaurant.describe_restaurant()
restaurant.open_restaurant()
