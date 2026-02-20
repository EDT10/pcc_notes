"""
Combine the two programs from Exercise 10-11 into one file. If the number is 
already stored, report the favorite number to the user. If not, prompt for the 
user's favorite number and store it in a file. Run the program twice to see that it works.
"""

from pathlib import Path
import json

path = Path("user_favorite_number.json")

if path.exists():
    content = path.read_text()
    fav_number = json.loads(content)
    print(f"Your favorite number is {fav_number}.")
else:
    user_fav_num = input("What is your favorite number? ")
    contents = json.dumps(user_fav_num)
    path.write_text(contents)
    print("Thanks I will remember that")


# Book solution below using error handling.

try:
    contents = path.read_text()
except FileNotFoundError:
    number = input("What's you favorite number?")
    contents = json.dumps(number)
    path.write_text(contents)
    print("Thanks, I will remember that.")
else:
    number = json.loads(contents)
    print(f"I know your favorite number! it's {number}")