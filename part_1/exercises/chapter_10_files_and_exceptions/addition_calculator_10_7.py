"""
Wrap your code from Exercise 10-6 in a while loop so the user can continue 
entering numbers even if they make a mistake and enter text instead of a number.
"""

print("Enter 2 numbers to add. Press 'q' to quit")


def adding_numbers(num_1, num_2):
    """Adds two numbers together"""
    try:
        total = int(num_1) + int(num_2)
    except ValueError:
        print("ERROR: I can only add numbers")
    else:
        print(f"The total number is {total}")

while True:
    first_number = input("Please enter your first number. ")
    if first_number.lower() == "q":
        break
    second_number = input("Please enter your second number to add. ")
    if second_number.lower() == "q":
        break

    adding_numbers(first_number, second_number)