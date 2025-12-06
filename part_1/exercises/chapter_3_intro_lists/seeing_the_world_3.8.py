places = ["London", "Ghana", "Japan", "Portugal", "Brazil"]

print(f"Original list: {places}\n")

print(f"Sorted: {sorted(places)}\n")

print(f"Original list: {places}\n")

print(f"Reverse sorted {sorted(places, reverse=True)}\n")

print(f"Original list: {places}\n")


places.reverse()
print(f"Original list reversed: {places}\n")

places.reverse()
print(f"Back to original using reverse: {places}\n")


places.sort()
print(f"Sort aplhabetically: {places}\n")

places.sort(reverse=True)
print(f"reversed Sort aplhabetically: {places}\n")