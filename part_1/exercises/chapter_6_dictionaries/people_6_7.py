person_1 = {
    "first_name": "saca",
    "last_name": "dinho",
    "age": 29,
    "city": "laurel",
}

person_2 = {
    "first_name": "aristide",
    "last_name": "manga",
    "age": 28,
    "city": "bowie",
}


person_3 = {
    "first_name": "dave",
    "last_name": "bravo",
    "age": 31,
    "city": "elkridge",
}


people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person["first_name"]} {person["last_name"]}"
    print(f"{full_name.title()} is {person["age"]} and lives in {person["city"].title()}")