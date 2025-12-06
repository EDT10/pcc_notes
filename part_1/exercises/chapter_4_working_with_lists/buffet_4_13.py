original_menu = ("donut", "jollof", "potatoes greens", "cassava leaves", 
                 "dry rice and fried fish")

print("*****This is our menu*****\n")

for food in original_menu:
    print(food.title())


#This is not valid because you can't change items in a tuple
# original_menu[0] = "meat pie"

new_menu = ("meat pie", "jollof", "potatoes greens", "fried rice", 
            "dry rice and fried fish")

print("\n##### This is NEW menu #####\n")

for food in new_menu:
    print(food.title())