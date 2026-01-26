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

