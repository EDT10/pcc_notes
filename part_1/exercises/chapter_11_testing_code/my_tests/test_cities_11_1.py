from city_functions_11_1 import city_country

def test_city_country():
    """Does Santiago and Chile work?"""
    formatted_string = city_country("santiago", "chile")
    assert formatted_string == "Santiago, Chile"
