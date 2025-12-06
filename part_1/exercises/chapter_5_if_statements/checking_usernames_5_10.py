current_usernames = ["the_bosD123", "admin", "bidLion890", "Dbomb321", "wesh"]

new_users = ["thosd123", "ADMIN", "bidE890", "bRavo", "Wesh"]

current_usernames_lower = []

# list comprehension version. make a copy of current username list and make the 
# item lower case and add them to the new list current_usernames_lower.
current_usernames_lower = [user.lower() for user in current_usernames]

#long version
for current_username in current_usernames:
    current_usernames_lower.append(current_username.lower())


for new_user in new_users:
    if new_user.lower() in current_usernames_lower:
        print(f"Sorry, the username {new_user} already exist")
    else:
        print(f"Welcome new user: {new_user}")