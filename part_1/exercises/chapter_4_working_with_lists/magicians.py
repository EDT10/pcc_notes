magicians = ["alice", "david", "carolina"]

#assigning each item in the list to the temporary variable call magician
for magician in magicians:
    #These set of steps are repeated once for each item in the list.
    print(f"{magician.title()}, you performed a great trick")
    print(f"I can't wait to see your next trick {magician.title()}\n")

#code is excuted once after the for loop. No repeated becuase it is not indented in the for loop block
print("Thank you, everyone. That was a great magic show")

