"""
An administrator is a special kind of user. Write a class called Admin that inherits 
from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 
Add an attribute, privileges, that stores a list of strings like "can add post", 
"can delete post", "can ban user", and so on. Write a method called show_privileges() 
that lists the administrator's set of privileges. Create an instance of Admin, and call your method.
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


class Admin(User):
    """Simulating an admin user with special privileges"""
    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name, age, location, gender)
        self.privileges = ["Can add post", "Can delete post", "Can ban user"]

    def show_privileges(self):
        """Shows all the privileges for an admin user."""
        print(f"This is what {self.first_name} can do as an Admin.")        
        for privilege in self.privileges:
            print(f"- {privilege}.")

admin_1 = Admin("Vye", "Sim", 27, "DC", "Female")

admin_1.describe_user()
admin_1.show_privileges()
