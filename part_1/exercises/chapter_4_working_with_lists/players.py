players = ["charles", "martina", "michael", "florence", "eli"]

#slicing a list. Python stops one item before the second index you specify.
print(players[0:3])

print(players[1:4])

#If you omit the first index, Python automatically starts at the beginning of the list.
print(players[:4])

#if you omit the second index, Python starts from the first index provided through the end of the list

print(players[1:])

#You can output any slice from the end of the list using a negative index.
print(players[-3:])


print("\nHere are the first 3 players on my team")

#using for loop for a slice
for player in players[0:3]:
    print(player.title())