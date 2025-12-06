available_toppings = ["mushroom", "olives", "extra cheese", "green peppers",
                      "pepperoni", "pineapple"]

requested_toppings = ["mushroom", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")