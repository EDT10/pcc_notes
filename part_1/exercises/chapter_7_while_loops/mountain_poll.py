responses = {}
# Set a flag to indicate that polling is active.

polling_active = True

while polling_active:
    # prompt for the person's name and response.
    name = input(f"\nWhat is your name? ")
    response = input("Which mountian would you like to climb someday? ")

    # Store the response in the dictionary with name as key and response as 
    # value
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")

    if repeat == "no":
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")

for name, response in responses.items():
    print(f"{name} would like to climb {response}.")

