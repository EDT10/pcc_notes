# Printing ordinal numbers which indicate their postitions in a list
# ex 1st, 2nd, 3rd, etc


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_num = numbers[:]

print(new_num)

# shorter way of creating and looping through a list using the range function 
# inside the list function.
for num in list(range(1, 10)):
    if num == 1:
        print(f"{num}st.")
    elif num == 2:
        print(f"{num}nd.")
    elif num == 3:
        print(f"{num}rd.")
    else:
        print(f"{num}th.")