
# Defining a class called Dog. Capitalized name refer to classes in Python
# No parenthesis when defining this class because its been created from scratch.
class Dog:
    """A simple attempt to model a dog."""

    # __init__ a special method that Python runs automatically whenever we create
    # a new instance based on the class. self refers to that particular instance being
    # created from the class.
    def __init__(self, name, age):
        """Initialize name and age"""
        self.name = name
        self.age = age
    # methods with parameter of self means each instance from the class have access to 
    # these methods.
    def sit(self):
        """simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# making an instance of dog from the Dog class
my_dog = Dog("Willie", 6)

# Accessing the attributes in the Dog class
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

#Access the methods defined in the Dog class.
my_dog.sit()
my_dog.roll_over()

your_dog = Dog("Lucy", 3)

print(f"\nYour dog name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

your_dog.sit()