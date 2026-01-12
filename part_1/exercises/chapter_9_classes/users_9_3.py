"""
Make a class called User. Create two attributes called first_name and last_name, 
and then create several other attributes that are typically stored in a user profile. 
Make a method called describe_user() that prints a summary of the user's information.
Make another method called greet_user() that prints a personalized greeting to the user.

Create several instances representing different users, and call both methods for each user.
"""

class User:
    """Modeling a typical user profile"""

    def __init__(self, first_name, last_name, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender

    def describe_user(self):
        "Summarizes the attributes of the user profile"
        print(f"{self.first_name} {self.last_name} is a {self.age} years old {self.gender}" 
              f" and is located in {self.location}.")

    def greet_user(self):
        """Greets user using first name and location"""
        print(f"Hello {self.first_name} from {self.location}!\n")


emma = User("Emma", "watson", 29, "Maryland", "female")

emma.describe_user()
emma.greet_user()

dave = User("Dave", "GG", 31, "DC", "male")
dave.describe_user()
dave.greet_user()