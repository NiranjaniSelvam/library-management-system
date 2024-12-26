1. README File 

Library Management System

Overview
This is a simple Library Management System built using Python. It allows users to:
- Add books to the library.
- Borrow books.
- Return books.
- View all available books in the library.

The system ensures that books can only be borrowed if they are available, and it keeps track of borrowed books by marking them as unavailable. The system also allows users to return books and make them available again.

Features
- Add books: Add books with unique ISBN, title, author, and publication year.
- Borrow books: Borrow a book if it is available.
- Return books: Return borrowed books, making them available again.
- View available books: View a list of books that are currently available for borrowing.

Installation

Prerequisites
Make sure you have the following installed:
- Python 3.x
- Git

Setting Up the Project
1. Clone the repository:
   git clone https://github.com/your-username/library-management-system.git

2. Navigate to the project directory:
   cd library-management-system

3. Set up a virtual environment (optional but recommended):
   python3 -m venv venv

4. Activate the virtual environment:
   - Windows:
     venv\Scripts\activate
   - Mac/Linux:
     source venv/bin/activate

5. Install the required dependencies (for running tests):
   pip install pytest

Usage

Running Tests
1. To run the tests for the Library Management System, use pytest:
   pytest

   This will run all the test cases and show the results in the terminal.

Adding Books
You can add books using the add_book method:
library = Library()
library.add_book("12345", "Python Basics", "John Doe", 2023)

Borrowing Books
To borrow a book, use the borrow_book method with the book's ISBN:
library.borrow_book("12345")

Returning Books
To return a borrowed book, use the return_book method with the book's ISBN:
library.return_book("12345")

License
This project is licensed under the MIT License.

2. Test Report 
Test Report - Library Management System

Overview
This test report contains the results of the unit tests for the Library Management System. The tests were written using pytest to ensure the core functionalities of adding, borrowing, and returning books work as expected.

Test Cases

1. test_add_book
- Description: Tests the functionality of adding a book to the library.
- Result: Passed
- Details: A book with ISBN "12345", title "Python Basics", author "John Doe", and year 2023 was added successfully. The book appears in the list of available books.

2. test_borrow_book
- Description: Tests the functionality of borrowing a book from the library.
- Result: Passed
- Details: After borrowing the book with ISBN "12345", the available books list is empty, confirming the book is no longer available.

3. test_borrow_unavailable_book
- Description: Tests borrowing a book that is already borrowed.
- Result: Passed
- Details: The second attempt to borrow the book with ISBN "12345" raised a ValueError, with the message "Book not available".

4. test_return_book
- Description: Tests the functionality of returning a borrowed book.
- Result: Passed
- Details: After borrowing the book with ISBN "12345", returning it makes the book available again, as confirmed by the available books list.

5. test_return_book_not_borrowed
- Description: Tests returning a book that has not been borrowed.
- Result: Passed
- Details: Attempting to return a book that was not borrowed raises a ValueError, with the message "Book not found or already returned".

Test Summary

- Total Tests: 5
- Passed: 5
- Failed: 0

Test Environment:
- Python version: 3.x
- pytest version: 7.x

Conclusion
All tests passed successfully, confirming that the core features of the Library Management System (adding books, borrowing books, and returning books) work as expected.
