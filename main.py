from library import Library

def main():
    lib = Library()

    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Register User")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Show Books")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            book_id = input("Book ID: ")
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(book_id, title, author)

        elif choice == "2":
            user_id = input("User ID: ")
            name = input("Name: ")
            lib.register_user(user_id, name)

        elif choice == "3":
            book_id = input("Book ID: ")
            user_id = input("User ID: ")
            lib.issue_book(book_id, user_id)

        elif choice == "4":
            book_id = input("Book ID: ")
            user_id = input("User ID: ")
            lib.return_book(book_id, user_id)

        elif choice == "5":
            lib.show_books()

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
