import pytest
from library_management.library import Library

def test_add_book():
    library = Library()
    library.add_book(isbn="12345", title="Python Basics", author="John Doe", year=2023)
    books = library.view_available_books()
    assert len(books) == 1
    assert books[0]['isbn'] == "12345"
