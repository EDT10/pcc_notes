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
    


# This calls the __init__() method defined in ElectricCar, which in turn tells Python
# to call the __init__() method defined in the parent class Car.
my_leaf = ElectricCar("nissan", "leaf", 2024)

# calling methods from the parent Class
print(my_leaf.get_descriptive_name())
my_leaf.update_odometer(23_909)
my_leaf.read_odometer()

# calling the battery Class as attribute which is a instance of child class ElectricCar.
print()

my_leaf.battery.battery_size = 65
my_leaf.battery.describe_battery()

my_leaf.battery.get_range()