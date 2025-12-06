squares = []

for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

#list comprehension does the same thing as above but combines everything in one line.

numbers = [number**2 for number in range(1, 11)]
print(numbers)