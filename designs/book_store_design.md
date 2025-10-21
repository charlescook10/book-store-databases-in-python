# Book Model and Repository Classes Design Recipe

## 1. Design and create the Table


## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)
class Book


# Repository class
# (in lib/book_repository.py)
class BookRepository

```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: books

# Model class
# (in lib/book.py)

class Book:
    def __init__(self, title, author_name):
        self.id = 0
        self.title = title
        self.author_name = author_name

# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> book = Book()
# >>> book.title = "Moby Dick"
# >>> book.author_name = "Herman Melville"
# >>> book.title
# 'Moby Dick'
# >>> book.author_name
# 'Herman Melville'

```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: books

# Repository class
# (in lib/book_repository.py)

class BookRepository():

    # Selecting all records
    # No arguments
    def all():
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of Book objects.

        # Gets a single record by its ID
        # One argument: the id (number)
    def find(id):
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books WHERE id = $1;

        # Returns a single Book object.

        # Add more methods below for each operation you'd like to implement.

    # def create(book)
    # 

    # def update(book)
    # 

    # def delete(book)
    # 

```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

```python
# EXAMPLES

# 1
# Get all books

repo = BookRepository()

books = repo.all()

len(books) # =>  2

books[0].id # =>  1
books[0].title # =>  'Moby Dick'
books[0].author_name # =>  'Herman Melville'

books[1].id # =>  2
books[1].title # =>  '1984'
books[1].author_name # =>  'George Orwell'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._