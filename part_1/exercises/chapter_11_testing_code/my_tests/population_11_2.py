def city_country(city, country, population=""):
    """ Returns a string with city, county and population"""
    if population:
        return f"{city.title()}, {country.title()} - population {population}"
    else:
        return f"{city.title()}, {country.title()}"