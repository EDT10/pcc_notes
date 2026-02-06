"""
Write a while loop that prompts users for their name. Collect all the names 
that are entered, and then write these names to a file called guest_book.txt. 
Make sure each entry appears on a new line in the file.
"""

from pathlib import Path

path = Path("./guest_book.txt")

# collect names
prompt = "\nPlease enter your name to be added to the guest book."
prompt += "\nType quit to end."

guest_list = [ ]

# store names
while True:
    guest_names = input(prompt)

    if guest_names.lower() == "quit":
        break

    print(f"Thanks {guest_names}, adding you to the guest book.")
    guest_list.append(guest_names)

# build a string
file_string = ""
for name in guest_list:
    file_string += f"{name}\n"

# write to file
path.write_text(file_string)

