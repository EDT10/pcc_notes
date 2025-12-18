def make_album(firstname, album, lastname=None, num_of_song=None):
        #starting dictionary. This is a practice for functions because an album with no songs 
        # makes no sense.
        album_info = {
        "firstname": firstname,
       # "lastname": lastname,
        "album": album,
        # "number_of_songs": num_of_song,
        }
            
        # change dictionary if lastname and number of songs is provided.
        if lastname and num_of_song:
            album_info = {
            "firstname": firstname,
            "lastname": lastname,
            "album": album,
            "number_of_songs": num_of_song,
            }
        # change dictionary if only number of songs is provided.
        elif num_of_song:            
            album_info = {
            "firstname": firstname,
            #"lastname": lastname,
            "album": album,
            "number_of_songs": num_of_song,
            }
        # change dictionary if only lastname is provided.
        elif lastname:          
            album_info = {
            "firstname": firstname,
            "lastname": lastname,
            "album": album,
            #"number_of_songs": num_of_song,
            }   

        print(f"{album_info}\n")

while True:
    print(f"Please enter album information below.\n\t type 'q' to quite")

    firstname = input("Enter artist firstname: ")
    if firstname == "q":
        break

    lastname = input("Enter artist lastname: ")
    if lastname == "q":
        break

    album = input("Name of album: ")
    if album == "q":
        break

    num_of_song = input("Number of songs: ")
    if num_of_song == "q":
        break
    
    # Using keyword argument to avoid confusion and maintain the order in which the 
    #items in the dictionary are printed.
    album_info = make_album(firstname=firstname, lastname=lastname, album=album, num_of_song=num_of_song)


