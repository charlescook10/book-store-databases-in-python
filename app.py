from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.book_repository import BookRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/book_store.sql")

# # Retrieve all artists
# artist_repository = ArtistRepository(connection)
# artists = artist_repository.all()

# # Retrieve all albums
# album_repository = AlbumRepository(connection)
# albums = album_repository.all()

# # List them out
# for artist in artists:
#     print(artist)

# for album in albums:
#     print(album)

# Retrieve all albums
book_repository = BookRepository(connection)
books = book_repository.all()

for book in books:
    print(book)