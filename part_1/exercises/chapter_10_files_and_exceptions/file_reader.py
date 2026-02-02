from pathlib import Path

# build a Path object representing the file pi_digits.txt and assign to variable
# path.
path = Path("./pi_digits.txt")

contents = path.read_text()

contents = contents.rstrip()
lines = contents.splitlines()
for line in lines:
    print(line)