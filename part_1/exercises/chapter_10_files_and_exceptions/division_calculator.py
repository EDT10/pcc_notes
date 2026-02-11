
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit. ")

while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    
    # run this code first.
    try:
        answer = int(first_number) / int(second_number)
    # if a ZeroDivisionError occurs let the user know.
    except ZeroDivisionError:
        print("You can't divide by 0!")
    # run this code if the code in the try block runs successfully.
    else:
        print(answer)