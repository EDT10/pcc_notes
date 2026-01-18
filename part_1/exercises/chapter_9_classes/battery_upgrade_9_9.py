"""
Use the final version of electric_car.py from this section. 
Add a method to the Battery class called upgrade_battery(). 
This method should check the battery size and set the capacity to 65 if it isn't already. 
Make an electric car with a default battery size, call get_range() once, 
and then call get_range() a second time after upgrading the battery. 
You should see an increase in the car's range.
"""

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initializing attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odemter!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self, battery_size=40):
        """"Initializing the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size >= 65:
            range = 225
        elif self.battery_size <= 40:
            range = 100

        print(f"A {self.battery_size}-kWh battery can go about {range} miles on full charge.")

    def upgrade_battery(self):
        """Upgrades battery to 65-kWh"""
        if self.battery_size <= 65: 
            self.battery_size = 65
               


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

cyber_truck = ElectricCar("Tesla", "Cyber Truck", 2026)

print(cyber_truck.get_descriptive_name())

cyber_truck.battery.battery_size = 30
cyber_truck.battery.describe_battery()
cyber_truck.battery.get_range()
cyber_truck.battery.battery_size = 65
print(f"\t...Upgrading batttery to {cyber_truck.battery.battery_size}-kWh...")
cyber_truck.battery.upgrade_battery()
cyber_truck.battery.describe_battery()
cyber_truck.battery.get_range()