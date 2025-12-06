#out is 1 to 4 excluding 5 because range stops at the second argument provided.
for value in range(1, 5):
    print (value)

#wrap the range() function in the list() function to convert the sequence of numbers into a list
numbers = list(range(1, 6))
print(numbers)

#The 3rd argument is used as a step to use to increment. This will increment by two between 2 and 11
even_numbers = list(range(2, 11, 2))
print(even_numbers)