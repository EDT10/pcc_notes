cities = {
    "paris": {
        "country": "france",
        "population": 1_000_000,
        "fact": "Known for the eiffel tower.",
    },
    "monrovia": {
        "county": "liberia",
        "population": 8_000,
        "fact": "Has the best jollof rice",
    },
    "cairo": {
        "country": "egypt",
        "population": 500_000,
        "fact": "Has all the Pharoahs."
    },
}

for city, city_facts in cities.items():
    print(f"\nHere is some information about {city.title()}.")

    for key, value in city_facts.items():
        print(f"\t{key.title()}: {value}")