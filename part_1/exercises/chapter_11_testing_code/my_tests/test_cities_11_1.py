from population_11_2 import city_country

def test_city_country():
    """Does Santiago and Chile work?"""
    formatted_string = city_country("santiago", "chile")
    assert formatted_string == "Santiago, Chile"

def test_city_country_population():
    """Does Santiago, Chile and 5_000_000 work?"""
    formatted_string = city_country("santiago", "chile", "5000000")
    assert formatted_string == "Santiago, Chile - population 5000000"