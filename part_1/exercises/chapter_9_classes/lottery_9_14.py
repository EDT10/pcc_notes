"""
Make a list or tuple containing a series of 10 numbers and 5 letters. 
Randomly select 4 numbers or letters from the list and print a message saying 
that any ticket matching these 4 numbers or letters wins a prize.
"""
from random import choice

char = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C","D", "E"]

winning_combo = []

# pick 4 items randomly from the list and add them to the winning_combo list.
for pick in range(4):
    one_pick = choice(char)
    winning_combo.append(one_pick)

print(f"The winning ticket is: {winning_combo}")



