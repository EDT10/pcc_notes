alien_0 = {"color": "green", "points": 5}


# Access values in a dictionary.

print(alien_0["color"])

new_points = alien_0["points"]

print(f"You just earned {new_points}.")

# Adding new key-pair to the dictionary.
alien_0["x_position"] = 0
alien_0["y_position"] = 25

print(alien_0)

# Starting with an empty dictionary.
alien_1 = {}
alien_1["color"] = "red"
alien_1["points"] = 3

print(f"\nAlien 1 character: {alien_1}\n")

# Modifying a dictionary
alien_1["color"] = "yellow"

print(f"Alien 1 color is now {alien_1['color']}")

# Removing key-value pair from dictionary

del alien_1["color"]
print(alien_1)