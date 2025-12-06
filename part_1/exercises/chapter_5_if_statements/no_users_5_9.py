usernames = []

#checking if username is list is empty
if not usernames:
        print("We need more users")


for username in usernames:
    if username == "admin":
        print(f"\nWelcome {username}, You have all the privileges.")
    else:
        print(f"\nHello {username}, Enjoy the site.")