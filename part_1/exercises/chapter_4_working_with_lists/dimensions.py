#Tuple is defined by using parenthesis and are immutable. 
# Meaning they cannot be changed
dimensions = (200, 50, 30, 40, "food")

#Y ou can get items from a tuple just list with a list 
# using index position in a square bracket
print(dimensions[0])
print(dimensions[1])
print(dimensions[3])
print(dimensions[-1].title())

# You can loop over all the values in a tuple using a for loop, 
# just as you did with a list.
for dimension in dimensions:
    print(dimension)

print(dimensions)

# Although you can't modify a tuple, 
# You can assign a new value to a variable that represents a tuple.
dimensions = (100, 50, 99, 40, "slices")
print("\nModified dimensions")

for dimension in dimensions:
    print(dimension)

