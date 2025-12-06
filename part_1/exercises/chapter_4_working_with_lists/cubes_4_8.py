#Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10).
#use a for loop to print out the value of each cube.

#start with empty list
my_list = []

#iterate from 1 - 11
for num in range(1, 11):
    #take the current num and raise it to the 3rd power to find the cube
    cubes = num ** 3

    #add the cube to the empty list
    my_list.append(cubes)

print(my_list)

#list comprehension

first_cubes = [number ** 3 for number in range(1, 11)]
print(first_cubes)

