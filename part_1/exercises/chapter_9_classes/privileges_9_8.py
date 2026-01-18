"""
Write a separate Privileges class. The class should have one attribute, privileges, 
that stores a list of strings as described in Exercise 9-7. Move the show_privileges() 
method to this class. Make a Privileges instance as an attribute in the Admin class. 
Create a new instance of Admin and use your method to show its privileges.
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

class Privileges:
    """Class pecifically for users with admin roles."""
    def __init__(self, list_of_privileges=[]):
        self.privileges = list_of_privileges
    
    def show_privileges(self):
        """Shows all the privileges if account is an admin user."""
        print(f"List of admin rights:")  
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}.")
        else:
            print(f"\t-This is not a privileged User. Nothing to show.")


class Admin(User):
    """Simulating an admin user with special privileges"""
    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name, age, location, gender)

        #Initializing an empty set of privileges
        self.privileges = Privileges()

    

admin_1 = Admin("Vye", "Sim", 27, "DC", "Female")

admin_1.describe_user()
admin_1.privileges.show_privileges()

print(f"Adding admin rights to {admin_1.first_name}...")
admin_1.privileges.privileges = ["Can delete posts",
                                  "Can add users",
                                  "Can ban users"]
admin_1.privileges.show_privileges()