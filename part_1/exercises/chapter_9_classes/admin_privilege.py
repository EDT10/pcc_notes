from admin_users import User

class Privileges:
    """Class pecifically for users with admin roles."""
    def __init__(self, list_of_privileges=[]):
        self.list_of_privileges = list_of_privileges
    
    def show_privileges(self):
        """Shows all the privileges if account is an admin user."""
        print(f"List of admin rights:")  
        if self.list_of_privileges:
            for privilege in self.list_of_privileges:
                print(f"- {privilege}.")
        else:
            print(f"\t-This is not a privileged User. Nothing to show.")


class Admin(User):
    """Simulating an admin user with special privileges"""
    def __init__(self, first_name, last_name, age, location, gender):
        super().__init__(first_name, last_name, age, location, gender)

        #Initializing an empty set of privileges
        self.privileges = Privileges()