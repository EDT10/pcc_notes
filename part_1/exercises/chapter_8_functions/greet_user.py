def greet_user(username):
    """Displaying a simple greeting."""
    print(f"Hello, {username.title()}")

#greet_user("jesse")


# defining the function
def greet_all_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# creat list outside the function
usernames = ["hanna", "ty", "margot"]

#passing the list to the function so the items can be worked on individually.
greet_all_users(usernames)