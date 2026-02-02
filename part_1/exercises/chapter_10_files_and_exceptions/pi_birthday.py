from pathlib import Path

path  = Path("./pi_million_digits.txt")
content = path.read_text()

lines = content.splitlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy: ")

if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
    print(f"Its at the {pi_string.index(birthday) + 1}th place.")
else:
    print("Your birthday does not appear in the first  million digits of pi.")
