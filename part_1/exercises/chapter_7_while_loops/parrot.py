prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# using the "active" variable as flag to signal the current state of the program.
active = True

while active:
    message = input(prompt)

# if the user enters "quit", the active variable which is the flag is set to False.
# This ends the while loop
    if message == "quit":
        active = False
    else:
        print(message)






# message = " "

# while message != "quit":
#     message = input(prompt)

#     if message != "quit":
#         print(message)

