"""
Write a program that polls users about their dream vacation. 
Write a prompt similar to If you could visit one place in the world, 
where would you go? Include a block of code that prints the results of the poll.
"""

prompt = "If you could visit one place in the world, where would you go? "

poll_active = True
poll_results = { }

while poll_active:
    name = input("What is your name? ").title()
    place = input(f"{prompt}").title()
    
    poll_results[name] = place

    repeat = input("Will others be voting? Enter Yes or No. ").title()

    if repeat == "No":
        poll_active = False

for name, place in poll_results.items():
    print(f"{name}, would like to visit {place}")






