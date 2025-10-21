from lib.book import Book

"""
book constructs with an id, title, author_name
"""
def test_book_constructs():
    book = Book(1, "Test book", "Test")
    assert book.id == 1
    assert book.title == "Test book"
    assert book.author_name == "Test"

"""
We can format books to strings nicely
"""
def test_books_format_nicely():
    book = Book(1, "Test book", "Test")
    assert str(book) == "1 - Test book - Test"

"""
We can compare two identical books
And have them be equal
"""
def test_books_are_equal():
    book1 = Book(1, "Test book", "Test")
    book2 = Book(1, "Test book", "Test")
    assert book1 == book2
