prompt = "\nPlease enter a topping to be added to your pizza. "
prompt += "\n\tEnter 'quit' to exit. "

while True:
    topping_added = input(prompt)
    topping_added = topping_added.title()

    if topping_added == "Quit":
        print("Please come again, goodbye!")
        break
    else:
        print(f"Adding {topping_added} to your pizza.")