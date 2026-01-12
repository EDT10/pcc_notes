"""
Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 
Write a method called increment_login_attempts() that increments the value of 
login_attempts by 1. Write another method called reset_login_attempts() 
that resets the value of login_attempts to 0.

Make an instance of the User class and call increment_login_attempts() several 
times. Print the value of login_attempts to make sure it was incremented properly, 
and then call reset_login_attempts(). Print login_attempts again to make sure 
it was reset to 0.
"""

class User:
    """Modeling a typical user profile"""

    def __init__(self, first_name, last_name, age, location, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.gender = gender
        self.login_attempt = 0

    def describe_user(self):
        "Summarizes the attributes of the user profile"
        print(f"{self.first_name} {self.last_name} is a {self.age} years old {self.gender}" 
              f" and is located in {self.location}.")

    def greet_user(self):
        """Greets user using first name and location"""
        print(f"Hello {self.first_name} from {self.location}!\n")

    def increment_login_attempt(self):
        """Increments login attempts by 1"""
        self.login_attempt += 1
        print(f"{self.first_name} attempted to login {self.login_attempt} times.")

    def reset_login_attempt(self):
        """Resets login attempt to 0"""
        self.login_attempt = 0
        print(f"\n{self.first_name} login has been reset to {self.login_attempt}.")

emma = User("Emma","Watkins", 29, "DC", "Female")

emma.describe_user()
emma.increment_login_attempt()
emma.increment_login_attempt()
emma.increment_login_attempt()
emma.increment_login_attempt()

emma.reset_login_attempt()
emma.increment_login_attempt()
emma.increment_login_attempt()