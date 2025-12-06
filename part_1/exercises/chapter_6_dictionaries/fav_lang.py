favorite_languages = {
    "jen": ["python", "rust"],
    "sarah": ["c"],
    "edward": ["rust", "go"],
    "phil": ["python", "haskell"],
}

for name, languages in favorite_languages.items():
    # get the current name/key in the dictionary and print out a message
    print(f"\n{name.title()}'s favorite languages are:")
    
    # loop through the current languages/values which is a python list that is 
    # associated with the current name/key
    for language in languages:
        print(f"\t{language.title()}")