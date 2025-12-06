prompt = "\nPlease enter a topping to be added to your pizza. "
prompt += "\n\tEnter 'quit' to exit. "


# create empty list to track the number of toppings the user added
# flag variable to start the pizza order
#variable to track the maximum toppings you can have on the pizza

toppings = [ ]
maximum_toppings = True
toppings_remaining = 3

while maximum_toppings:
    topping_added = input(prompt).title()
    
    
    if topping_added == "Quit":
        print("Please come again, goodbye!")
        break
    
# Check for duplicates toppings in the list
    if topping_added in toppings:
        print(f"{topping_added} is already added, add a different topping.")
        continue
# add the user toppings to the list of toppings 
# subtract 1 from the current value of toppings remaining
    else:
        toppings.append(topping_added)
        print(f"Adding {topping_added} to your pizza.")
        toppings_remaining -= 1   

# break out of the loop when the toppings added is 3
# inform the user about the number of toppings they have left to add on their pizza.
    if (len(toppings)) > 2:
        print(f"\nyou have reached your limit of 3 toppings:")
        for tops in toppings:
            print(f"\t- {tops}")
        print("\nThank you for ordering! Please come again.")
        maximum_toppings = False
    else:
        print(f"\nYou have {toppings_remaining} toppings left to add on your pizza.")
        