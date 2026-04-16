from book import Book
from user import User

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully!")

    def register_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)
        print("User registered successfully!")

    def issue_book(self, book_id, user_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if book and user:
            if not book.is_issued:
                book.is_issued = True
                user.borrow_book(book)
                print("Book issued successfully!")
            else:
                print("Book already issued!")
        else:
            print("Invalid book or user ID!")

    def return_book(self, book_id, user_id):
        book = next((b for b in self.books if b.book_id == book_id), None)
        user = next((u for u in self.users if u.user_id == user_id), None)

        if book and user:
            if book in user.borrowed_books:
                book.is_issued = False
                user.return_book(book)
                print("Book returned successfully!")
            else:
                print("This user didn’t borrow this book!")
        else:
            print("Invalid book or user ID!")

    def show_books(self):
        for book in self.books:
            print(book)
