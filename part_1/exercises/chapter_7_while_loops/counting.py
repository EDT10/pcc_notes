current_number = 0

while current_number <= 10:
    current_number += 1
    
    # The continue statement tells Python to ignore the rest of the loop and 
    # return to the beginning
    if current_number % 2 == 0:
        continue

    print(current_number)