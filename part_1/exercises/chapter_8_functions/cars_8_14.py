"""
Write a function that stores information about a car in a dictionary. 
the function should always receive a manufacturer and a model name. 
It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, 
such as a color or an optional feature
"""

def make_car(manufacturer, model_name, **packages):
    """Car ordering system"""
    car = {
        "Manufacturer": manufacturer,
        "Model": model_name,
    }

    for key, value in packages.items():
        car[key] = value

    return car


car = make_car("subaru", "Outback", color="blue", tow_package=True)

print(car)
