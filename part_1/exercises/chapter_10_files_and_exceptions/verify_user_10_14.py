from pathlib import Path
import json

user_dictionary = { }

def get_stored_username(path):
    """
    Get stored user information from the new_user.json file if available.
    returns None if the file doesn't exist.
    """
    if path.exists():
        contents = path.read_text()
        # This line fails when the files exists but there is no content in it.
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """
    Prompt for new information and adds to the user_dictionary. 
    The dictionary is written to the new_user.json file. 
    Creates the new_user.json file if it doesn't exists.
    """    
    username = input("What is your username? ")
    first_name = input("What is your first name? ")
    city = input("What is your city? ")
    user_dictionary["Username"] = username
    user_dictionary["First Name"] = first_name
    user_dictionary["City"] = city
    contents = json.dumps(user_dictionary)
    path.write_text(contents)
    return user_dictionary


def greet_user():
    """ 
    verify if username is already entered and greets the user by username. 
    If the username is different, ask for user their information 
    """

    path = Path("new_users.json")
    user_data = get_stored_username(path)
    # if user_data exists confirm the username. If not, ask for new user data
    if user_data:
        confirm_username = input(f"Is your username {user_data["Username"]}? ")
        if confirm_username.lower() == "no":
            user_data = get_new_user_info(path)
            print(f"We'll remember you when you come back, {user_data["Username"]}!")
        else:
            print(f"Welcome back, {user_data["Username"]}!")
            print(f"Your name is {user_data["First Name"]} and your are from {user_data["City"]}!")
    else:
        user_data = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_data["Username"]}!")


greet_user()