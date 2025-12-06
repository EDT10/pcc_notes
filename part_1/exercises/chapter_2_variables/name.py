name = "ada loVelace"
#strings with methods

print(name.title())
print(name.upper())
print(name.lower())
print(name.capitalize())

first_name = " emmanuel "
last_name = "wright"

full_name = f"{first_name} {last_name}"

print(f"Hello, {full_name.title()}!")
print()
#new line character (\n) and tab character (\t)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

#Removing white spaces
print()
print(first_name.lstrip())
print(first_name.rstrip())
print(first_name.strip())

print()

#removing prefixes from url
nostarch_url = "https://nostarch.com"
print(nostarch_url.removeprefix("https://"))