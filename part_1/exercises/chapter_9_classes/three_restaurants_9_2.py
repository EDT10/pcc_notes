"""
Start with your class from Exercise 9-1. Create three different instances from
the class, and call describe_restaurant() for each instance.
"""

class Restaurant:
    """Modeling a restaurant"""

    def __init__(self, restaurant_name, cousine_type):
        self.restaurant_name = restaurant_name
        self.cousine_type = cousine_type

    def descriibe_restaurant(self):
        """Describing the restaurant."""
        print(f"The name of the restaurant is {self.restaurant_name}")
        print(f"{self.restaurant_name} specializes in {self.cousine_type} cousine.")

    def open_restaurant(self):
        """Simulating opening a restaurant"""
        print(f"{self.restaurant_name} is now OPEN!")


indian_restaurant = Restaurant("Chutney", "Indian")
indian_restaurant.descriibe_restaurant()
indian_restaurant.open_restaurant()

print()

east_african = Restaurant("Swahili Village", "East African")
east_african.descriibe_restaurant()
east_african.open_restaurant()

print()
american_restarant = Restaurant("Stanford Grill", "American")
american_restarant.descriibe_restaurant()
american_restarant.open_restaurant()