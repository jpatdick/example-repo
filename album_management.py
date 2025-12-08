class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        """ Parameters:
                album_name: stores the name of the album
                number_of_songs: The number of songs in the album
                album_artist: The artist who created the album"""
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

album1 = []

album1.append(Album("Purple Reighn", 17, "Future"))
album1.append(Album("Honest", 14, "Future"))
album1.append(Album("DS2", 14, "Future"))              
album1.append(Album("EVOL", 11, "Future"))
album1.append(Album("FUTURE", 17, "Future"))

album1.sort(key=lambda album: album.number_of_songs)

album1[0], album1[1] = album1[1], album1[0] 

album2 = []

album2.append(Album("Harder Than Ever", 16, "Lil Baby"))
album2.append(Album("Street Gossip", 14, "Lil Baby"))
album2.append(Album("My Turn", 20, "Lil Baby"))              
album2.append(Album("The Voice of the Heroes", 18, "Lil Baby & Lil Durk"))
album2.append(Album("It's Only Me", 23, "Lil Baby"))

for album in album1:
    print(album)

print()

album2.extend(album1)

album2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
album2.append(Album("Oops!...I Did It Again", "Britney Spears", 16))

album2.sort(key=lambda album: album.album_name)

for album in album2:
    print(album)

print()
#Search Function
search_name = "Dark Side of the Moon"
index = -1

for i in range(len(album2)):
    if album2[i].album_name == search_name:
        index = i
        break

if index != -1:
    print(f"\nAlbum '{search_name}' found at index: {index}")
else:
    print(f"\nAlbum '{search_name}' not found in album2")