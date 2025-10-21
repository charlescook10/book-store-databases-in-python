# Albums Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table
```
# EXAMPLE

Table: albums

Columns:
id | title | release_year | artist_id
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE albums RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.

INSERT INTO albums (title, release_year, artist_id) VALUES ('Doolittle', 1989, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Surfer Rosa', 1988, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Waterloo', 1974, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Super Trouper', 1980, 2);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Bossanova', 1990, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Lover', 2019, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Folklore', 2020, 3);
INSERT INTO albums (title, release_year, artist_id) VALUES ('I Put a Spell on You', 1965, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Baltimore', 1978, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Here Comes the Sun', 1971, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Fodder on My Wings', 1982, 4);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Ring Ring', 1973, 2);

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 music_library < music_library.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: albums

# Model class
# (in lib/album.py)
class Album


# Repository class
# (in lib/album_repository.py)
class AlbumRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: albums

# Model class
# (in lib/album.py)

class Album:
    def __init__(self):
        self.id = 0
        self.title = ""
        self.release_year = 0
        self.artist_id = 0

        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> album = Album()
# >>> album.title = "Doolittle"
# >>> album.release_year = 1989
# >>> album.artist_id = 1
# >>> album.title
# 'Doolittle'
# >>> album.release_year
# 1989

```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: albums

# Repository class
# (in lib/album_repository.py)

class AlbumRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums;

        # Returns an array of Album objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, title, release_year, artist_id FROM albums WHERE id = $1;

        # Returns a single Album object.

        # Add more methods below for each operation you'd like to implement.

    # def create(album)
    # 

    # def update(album)
    # 

    # def delete(album)
    # 

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all albums

repo = AlbumRepository()

albums = repo.all()

len(albums) # =>  12

albums[0].id # => 1
albums[0].title # => 'Doolittle'
albums[0].release_year # => 1989

albums[11].id # => 12
albums[11].title # => 'Ring Ring'
albums[11].release_year # => 1973

# 2
# Get a single album

repo = AlbumRepository()

album = repo.find(3)

albums.id # =>  1
albums.title # =>  'Waterloo'
albums.release_year # =>  1974
albums.artist_id # =>  2

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._