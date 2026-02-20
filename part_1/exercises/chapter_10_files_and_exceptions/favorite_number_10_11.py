"""Write a program that prompts for the user's favorite number. Use json.dumps() 
to store this number in a file. Write a separate program that reads in this 
value and prints the message, 'I know your favorite number! It's _____.
'"""

from pathlib import Path
import json


user_fav_num = input("What is your favorite number? ")

# file to be written to
path = Path("user_favorite_number.json")
# take user fav number and convert to json format.
contents = json.dumps(user_fav_num)
# write the converted format to the file
path.write_text(contents)

print("Thanks I will remember that")