rsvp = input("How many people are in your party? ")
rsvp = int(rsvp)

if rsvp > 8:
    print(f"For a party of {rsvp}, you will have to wait for a table.")
else:
    print(f"We currently have a table available for {rsvp}.")