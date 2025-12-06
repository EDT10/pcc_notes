motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles)

#Modying the list
motorcycles[0] = "ducati"

print(motorcycles)

#adding item at the end of the list
motorcycles.append("toyota")

print(motorcycles)

#inserting item to the list
motorcycles.insert(0, "nissan")
print(motorcycles)


#removing item from the list base on its postion
del motorcycles[2]

print(motorcycles)

#pop() remove the last item in a list, but lets you work with that item after removing it

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#pop() also allows  you to removed items based on their index position. The item is no longer in the list.

first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was {first_owned.title()}")
print(motorcycles)

#.remove() method is used to removed item from the list based on its value not index postion. remove() method deletes only the first 
#occurrence of the value. You will need to use a loop to make sure all occurrences of the value are removed.

too_expensive = "ducati"
motorcycles.remove(too_expensive)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print(motorcycles)