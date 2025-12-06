pets = []

pet = {
    "type": "cat",
    "owner": "emmanuel",
}

pets.append(pet)

pet = {
    "type": "dog",
    "owner": "saca",
}

pets.append(pet)

pet = {
    "type": "bird",
    "owner": "vyness",
}

pets.append(pet)

pet = {
    "type": "snake",
    "owner": "wesh",
}

pets.append(pet)

for animal in pets:
    print()
    print("Pet info:")
    for key, value in animal.items():
        print(f"{key.title()}: {value.title()}")