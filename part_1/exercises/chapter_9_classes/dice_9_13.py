"""
Make a class Die with one attribute called sides, which has a default value of 6. 
Write a method called roll_die() that prints a random number between 1 and the 
number of sides the die has. Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint

class Die:
    """Making a die"""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """
        simulating a roll of a die and returns a random int between 1 
        and the given number of sides for the die.
        """
        choice = randint(1, self.sides)
        return choice


six_sided_die = Die()

print(f"\t ##### 6 sided die #####")
for num in range(10):
    side_up = six_sided_die.roll_die()
    print(f"{side_up} is facing up.")


ten_sided_die = Die()
ten_sided_die.sides = 10

print(f"\t ##### 10 sided die #####")
for num in range(10):
    side_up = ten_sided_die.roll_die()
    print(f"{side_up} is facing up.")


twenty_sided_die = Die()
twenty_sided_die.sides = 20

print(f"\t ##### 20 sided die #####")
for num in range(10):
    side_up = twenty_sided_die.roll_die()
    print(f"{side_up} is facing up")
