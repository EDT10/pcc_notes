cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original order: {cars}\n")
#sorting list alphabetically. This is a permanent change.
cars.sort()

print(f"Sorted permanently: {cars}\n")

#sorting list in reverse order alphabetically. This is a permanent change.
cars.sort(reverse=True)

print(f"Permanently sorted in reverse order: {cars}\n")

#sorting list alphabetically using the sorted() function. This is a temporary change.
print(f"Temporary sorted order from reverse order {sorted(cars)}\n")

#sorting list alphabetically using the sorted() function in reverse order. This is a temporary change.
print(f"Temporary sorted order from list above {sorted(cars, reverse=True)}\n")

# print(f"Back to reverse order again: {cars}\n")

cars = ["bmw", "audi", "toyota", "subaru"]
print(f"Original order: {cars}\n")

cars.reverse()
print(f"Non-aplhabetical reverse order: {cars}")

#get the list lenght of the list

print(f"\nThere are {len(cars)} cars in the list")