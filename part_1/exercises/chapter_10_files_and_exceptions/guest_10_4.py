from pathlib import Path

path = Path("./guest.txt")

guest_name = input("Please enter your name to be added to the guest book. ")

path.write_text(guest_name)
print(f"Thanks {guest_name}, you have been added to the guest book")