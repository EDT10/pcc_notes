favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

users = ["phil", "sarah", "adam", "john", "jen", "edward"]

for user in users:
    if user in favorite_languages.keys():
        print(f"Thank you for taking the poll {user.title()}.")
    else:
        print(f"{user.title()}, you are invited to take the poll.")