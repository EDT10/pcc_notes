favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
    }

friends = ["phil", "sarah"]

for name in favorite_languages.keys():
    print(f"Hello, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")


# language = favorite_languages["sarah"].title()
# print(f"Sarah's favorite language is {language}.")



# Looping through all the key-value pairs in the dictionary using the 
# items() method.
for name, language in favorite_languages.items():
    print(f"\n{name.title()} favorite laguage is {language}")


# Looping through the keys only in the dictionary using the 
# keys() method.
for name in favorite_languages.keys():
    print(name.title())

# using the keys() method to find out if a particular key exists in the dictionary

if "erin" not in favorite_languages.keys():
    print("Erin, please take out poll")


# looping through the dictionary in a particular order using the sorted() function.

for name in sorted(favorite_languages.keys()):
    print(f"\n{name.title()}, thank you for taking the poll.")


# looping through the values only in the dictionary using the values() method.
print("The following languages were mentioned:")

for language in favorite_languages.values():
    print(f"{language.title()}")


# Getting unique values from the dictionary using the set() function.

print("The following languages were mentioned, unique values only:")
for language in set(favorite_languages.values()):
    print(f"{language.title()}")


