"""A set of classes that can used to represent electric cars."""

#importing the parent class from a separate module. Importing a module into a module
from car import Car

class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """"Initializing the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        elif self.battery_size <= 40:
            range = 100

        print(f"This car can go about {range} miles on full charge.")


# defining child Class with parent class in parentheses. Parent class must be in
# the same class and must appear before the child class
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.      """
        
        super().__init__(make, model, year)
        # making the Battery class as attributes.
        #Create a new instance of Battery
        self.battery = Battery()
    
