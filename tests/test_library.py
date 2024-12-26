import pytest
from library_management.library import Library

def test_add_book():
    """Test adding a book to the library."""
    library = Library()
    library.add_book("12345", "Python Basics", "John Doe", 2023)
    books = library.view_available_books()
    assert len(books) == 1
    assert books[0]["isbn"] == "12345"
    assert books[0]["title"] == "Python Basics"
    assert books[0]["author"] == "John Doe"
    assert books[0]["year"] == 2023
    assert books[0]["available"] is True

def test_borrow_book():
    """Test borrowing a book from the library."""
    library = Library()
    library.add_book("12345", "Python Basics", "John Doe", 2023)
    library.borrow_book("12345")
    books = library.view_available_books()
    assert len(books) == 0  # No books should be available after borrowing

def test_borrow_unavailable_book():
    """Test borrowing a book that is already borrowed."""
    library = Library()
    library.add_book("12345", "Python Basics", "John Doe", 2023)
    library.borrow_book("12345")
    with pytest.raises(ValueError, match="Book not available"):
        library.borrow_book("12345")

def test_return_book():
    """Test returning a borrowed book to the library."""
    library = Library()
    library.add_book("12345", "Python Basics", "John Doe", 2023)
    library.borrow_book("12345")
    library.return_book("12345")
    books = library.view_available_books()
    assert len(books) == 1  # The book should be available again

def test_return_book_not_borrowed():
    """Test returning a book that was not borrowed."""
    library = Library()
    library.add_book("12345", "Python Basics", "John Doe", 2023)
    with pytest.raises(ValueError, match="Book not found or already returned"):
        library.return_book("12345")
