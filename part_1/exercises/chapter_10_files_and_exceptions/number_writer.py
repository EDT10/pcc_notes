from pathlib import Path
import json

numbers = [2, 3, 5, 7, 11, 13]

# Create a file in which to store the list of numbers. Use .json extension.
path = Path("numbers.json")

# use json.dumps() to generate a string containing the JSON representation of the data we are working with
contents = json.dumps(numbers)

# Write the string to a file using the write_text() method.
path.write_text(contents)