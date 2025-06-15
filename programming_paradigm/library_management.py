# library_management.py

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {book.title}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {book.title}")
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        available = False
        for book in self._books:
            if book.is_available():
                print(f"{book.title} by {book.author}")
                available = True
        if not available:
            print("No books are currently available.")
