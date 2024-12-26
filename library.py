class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self.books = []
//adding books
    def add_book(self, isbn, title, author, year):
        """
        Add a book to the library.
        
        :param isbn: Unique identifier for the book.
        :param title: Title of the book.
        :param author: Author of the book.
        :param year: Publication year of the book.
        """
        self.books.append({
            "isbn": isbn,
            "title": title,
            "author": author,
            "year": year,
            "available": True
        })
//viewing books
    def view_available_books(self):
        """
        View all books that are currently available for borrowing.
        
        :return: List of available books.
        """
        return [book for book in self.books if book["available"]]
//borrowing books
    def borrow_book(self, isbn):
        """
        Borrow a book from the library by ISBN.
        
        :param isbn: ISBN of the book to borrow.
        :raises ValueError: If the book is not available.
        """
        for book in self.books:
            if book["isbn"] == isbn and book["available"]:
                book["available"] = False
                return
        raise ValueError("Book not available")
//returning books
    def return_book(self, isbn):
        """
        Return a borrowed book to the library by ISBN.
        
        :param isbn: ISBN of the book to return.
        :raises ValueError: If the book is not found or already returned.
        """
        for book in self.books:
            if book["isbn"] == isbn and not book["available"]:
                book["available"] = True
                return
        raise ValueError("Book not found or already returned")
