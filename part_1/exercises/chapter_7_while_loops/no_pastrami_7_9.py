"""
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' 
appears in the list at least three times. Add code near the beginning of your 
program to print a message saying the deli has run out of pastrami, 
and then use a while loop to remove all occurences of 'pastrami' from sandwich_orders. 
Make sure no pastrami sandwiches end up in finished_sandiches.
"""

sandwich_orders = ["chicken", "pastrami", "avocado", "pastrami", "tuna", "pastrami"]
finished_sandwiches = [ ]

print("Deli has ran out of Pastrami sandwich\n")

# Remove every instance of pastrami sandwich from the list of sandwich orders
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")


while sandwich_orders:
    working_sandwich = sandwich_orders.pop()

    print(f"I am working on your {working_sandwich}")

    finished_sandwiches.append(working_sandwich)
        
print("\n")
for sandwich in finished_sandwiches:
    print(f"Here is your {sandwich} sandwich")