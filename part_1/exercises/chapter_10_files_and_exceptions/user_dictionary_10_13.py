"""
The remember_me.py example only stores one piece of information, the username. 
Expand this example by asking for two more pieces of information about the user, 
then store all the information you collect in a dictionary. Write this dictionary 
to a file using json.dumps(), and read it back in using json.loads(). Print a summary 
showing exactly what your program remembers about the user.
"""

from pathlib import Path
import json

user_dictionary = { }

def get_stored_username(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        # This line fails when the files exists but there is no content in it.
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for new information."""
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
    """Greet the user by name."""
    path = Path("new_users.json")
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username["Username"]}!")
        print(f"Your name is {username["First Name"]} and your are from {username["City"]}!")
    else:
        username = get_new_user_info(path)
        print(f"We'll remember you when you come back, {username["Username"]}!")


greet_user()
