my_foods = ["pizza", "falafel", "carrot cake","jollof"]

#copying a list
friend_foods = my_foods[:]

my_foods.append("cannoli")
friend_foods.append("ice cream")

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print(f"\nThe first three items in my food list: {my_foods[:3]}")
print(f"\nThe middle items in my food list: {my_foods[1:3]}")
print(f"\nThe last three items in my food list: {my_foods[-3:]}")

