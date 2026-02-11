#Testing book solutions for exercises if it is different from my solution

try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)
except ValueError:
    print("Sorry, I really need a number.")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}")