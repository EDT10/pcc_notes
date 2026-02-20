from pathlib import Path
import json

# file that will be loaded for reading.
path = Path("user_favorite_number.json")
# Read the contents of the file
content = path.read_text()
# load the content into memory in json format
fav_number = json.loads(content)



print(f"Your favorite number is {fav_number}.")