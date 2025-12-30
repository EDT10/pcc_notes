
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""

    print(f"\nmaking a size {size} pizza with the following toppings:")
    for topping in toppings:
        print(topping)

# make_pizza(16, "pepperoni")

# make_pizza(12, "mushrooms", "green peppers", "extra cheese", "extra cheese")

