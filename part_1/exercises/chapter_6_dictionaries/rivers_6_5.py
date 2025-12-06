rivers = {"river nile": "egypt", "mississippi river": "usa", "amazon river": "brazil",}

for river, country in rivers.items():
    if country == "usa":
        country = country.upper()
        print(f"The {river.title()} run through {country}.")
    else:
        print(f"The {river.title()} run through {country.title()}.")

for river in rivers.keys():
    print(river.title())

for country in rivers.values():
    print(country.upper())