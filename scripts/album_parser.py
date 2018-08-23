"""
By: Kay Hudson

A script to generate a collection of contacts for the Address Book exercise.
"""
import csv


def parse_data(f):
    """Parse CSV file into a list of album objects."""
    albums = []
    with open(f) as doc:
        # Can be refactored to use csv.DictReader() which takes care of create_album and fields!
        album_list = csv.reader(doc, quotechar='"', delimiter=',', skipinitialspace=True)
        for album_data in album_list:
            album = create_album(album_data)
            albums.append(album)
    return albums


def create_album(data):
    """Notice how we already know the columns to expect."""
    return {
        'number': data[0],
        'year': data[1],
        'album': data[2],
        'artist': data[3],
        'genre': data[4],
        'subgenre': data[5]
    }


def get_album(title, albums):
    for album in albums:
        if album['album'] == title:
            return album

    return "Album could not be found."


def list_artists(albums):
    """Return a list of artists sorted alphabetically."""
    artists = []
    for album in albums:
        artists.append(album['artist'])

    return sorted(artists)


def get_genre(genre, albums):
    genres = []
    for album in albums:
        if album['genre'] == genre:
            genres.append(album)

    # If no albums in that genre are found ...
    if len(genres) == 0:
        return "No albums in that genre were found."

    return genres


def count_albums(albums):
    return len(albums)
