"""
Make a list called sandwich_orders and fill it with the names of various sandwiches. 
Then make an empty list called finished_sandwiches. Loop through the list of 
sandwich orders and print a message for each order, such as I made your tuna sandwich. 
As each sandwich is made, move it to the list of finished sandwiches. 
After all the sandwiches have been made, print a message listing each sandwich that was made.
"""

sandwich_orders = ["chicken", "avocado", "tuna"]
finished_sandwiches = [ ]

while sandwich_orders:
    # Take the last item in the sandwich order list and make that the working order
    working_order = sandwich_orders.pop()
    print(f"working on {working_order.title()} sandwich.")

    # Add the working order to the finished sandwich list
    finished_sandwiches.append(working_order)

# print out all the finished orders that are in the finished sandwich list.
for sandwich in finished_sandwiches:
    print(f"{sandwich.title()} sandwich order has been completed")