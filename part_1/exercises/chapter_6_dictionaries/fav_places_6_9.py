favorite_places = {
    "europe": ["london", "madrid", "paris"],
    "africa": ["monrovia", "accra"],
    "asia": ["tokyo", "beijing"]
}


for continent, cities in favorite_places.items():
    print(f"My favorite places in {continent.title()}:")
    for city in cities:
        print(f"\t{city.title()}")
