"""
Using your latest Restaurant class, store it in a module. Make a separate file 
that imports Restaurant. Make a Restaurant instance, and call one of Restaurant's 
methods to show that the import statement is working properly.
"""

from restaurant_only import Restaurant

hangry_joe = Restaurant("Hangry Joe", "American")
hangry_joe.describe_restaurant()

thai_place = Restaurant("Pho Pho", "Asian")
thai_place.describe_restaurant()
thai_place.open_restaurant()