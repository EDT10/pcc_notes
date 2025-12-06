user_number = input("Enter a number to check if it is a multiple of 10. ")

if int(user_number) % 10 == 0:
    print(f"{user_number} is a multiple of 10.")
else:
    print(f"{user_number} is not a multiple of 10.")