"""
Write a function called city_country() that takes in the name of a city and its country. 
The function should return a string formatted like this:
"Santiago, Chile"

Call your function with at least three city-country pairs, and print the values that are returned.
"""

def city_country(city, country):
   # print("-" * 5)
    city_info = f"{city}, {country}"

    return f"{city_info}"


formatted_info = city_country("DC", "USA")
print(formatted_info)

formatted_info = city_country("London", "UK")
print(formatted_info)

formatted_info = city_country("Monrovia", "Liberia")
print(formatted_info)