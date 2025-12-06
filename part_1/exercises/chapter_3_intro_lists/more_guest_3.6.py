# One of your guests can't make the dinner so find a replacement and add them to the list.
guest_list = ["Vyness", "Elyas", "Dave", "Aristide"]
print(guest_list)

guest_cancelled = "Aristide"
print(f"{guest_cancelled} can't make it. He cancelled")

#finding the index position of guest that cancelled so it can be replaced with new guest. The new guest will take that specific poistion
guest_position_in_list = guest_list.index(guest_cancelled)

#remove the guest name from the list.
guest_list.remove(guest_cancelled)
#print(guest_list)
new_guest = "emmanuel t"

#insert newly invited guest in the index position of the guest that cancelled. Provide the index position and the replacement value.
guest_list.insert(guest_position_in_list, new_guest.title())

#print updated list

print(f"Updated guest list: {guest_list}.\n\t See new intvitations below:\n ")

print(f"{guest_list[0].title()} is invited to birthday dinner.\n")
print(f"{guest_list[1].title()} is invited to birthday dinner.\n")
print(f"{guest_list[2].title()} is invited to birthday dinner.\n")
print(f"{guest_list[3].title()} is invited to birthday dinner.\n")

print("\nJust found a bigger table. I am inviting more guests")

guest_list.insert(0, "Chidi")
guest_list.insert(2, "Greatest")
guest_list.append("Solo")

print(f"{guest_list[0].title()} is invited to birthday dinner.\n")
print(f"{guest_list[1].title()} is invited to birthday dinner.\n")
print(f"{guest_list[2].title()} is invited to birthday dinner.\n")
print(f"{guest_list[3].title()} is invited to birthday dinner.\n")
print(f"{guest_list[4].title()} is invited to birthday dinner.\n")
print(f"{guest_list[5].title()} is invited to birthday dinner.\n")
print(f"{guest_list[6].title()} is invited to birthday dinner.\n")