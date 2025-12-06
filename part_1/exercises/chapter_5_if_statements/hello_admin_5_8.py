
usernames = ["the_bosd123", "admin", "bigLion_2", "Dbomb321"]

if not usernames:
        print("We need more users")


for username in usernames:
    if username == "admin":
        print(f"\nWelcome {username}, You have all the privileges.")
    else:
        print(f"\nHello {username}, Enjoy the site.")