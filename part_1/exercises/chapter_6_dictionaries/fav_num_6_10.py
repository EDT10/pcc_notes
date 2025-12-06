favorite_numbers = {
    "wesh": [8, 10,14],
    "saca": [2, 5, 7],
    "bravo": [23, 1, 14],
    "vyness": [4, 3, 9],
}

for name, fav_num in favorite_numbers.items():
    print(f"{name.title()} favorite numbers are:")
    for num in fav_num:
        print(num)