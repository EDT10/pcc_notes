"""
Modify the make_shirt() function so that shirts are large by default with a message 
that reads I love Python. Make a large shirt and a medium shirt with the default 
message, and a shirt of any size with a different message.
"""

def make_shirt(message="I love Python", size="Large"):
    print(f"\nShirt size: {size}\nMessage on shirt: {message}")


make_shirt()
make_shirt(size="Medium")
make_shirt(size="small", message="This book is great for beginners.")