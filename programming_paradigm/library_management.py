class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  # Tracks if the book is available for checkout

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {'Available' if self.available else 'Checked Out'}"
def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"Checked out: {book}")
                else:
                    print("Book is already checked out.")
                return
        print("Book not found.")

def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"Returned: {book}")
                else:
                    print("Book was not checked out.")
                return
        print("Book not found.")


class Library:
    def __init__(self):
        self.books = []  # List to store books in the library

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book}")
                return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        for book in self.books:
            print(book)

    def checkout_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.available:
                    book.available = False
                    print(f"Checked out: {book}")
                else:
                    print("Book is already checked out.")
                return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.available:
                    book.available = True
                    print(f"Returned: {book}")
                else:
                    print("Book was not checked out.")
                return
        print("Book not found.")
