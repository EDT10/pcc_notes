from pathlib import Path

path = Path("./pi_digits.txt")
content = path.read_text()

lines = content.splitlines()
pi_string = ""
for line in lines:
    pi_string += line.strip()

print(pi_string[:5])
print(len(pi_string))

