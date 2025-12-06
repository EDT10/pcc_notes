prompt = " \nPlease enter your age to get the best price. "

while True:
    age = input(prompt)

    # if age != int(age):
    #     print("\nPlease enter a valid age in numbers. ")
    #     continue

    age = int(age)

    if age < 3:
        price = 0        
    elif age < 12:
        price = 10
    elif age >= 12:
        price = 15

    print(f"Your ticket costs ${price}.")