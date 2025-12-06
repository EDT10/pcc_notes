users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}

# assign the keys of the dictionary users to the variable "username" and 
# assign the values to the variable "user_info" which is also a dictionary
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    # accessing the values of each key in the nested dictionary "user_info"
    full_name = f"{user_info["first"]} {user_info["last"]}"
    location = user_info["location"]

    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

    