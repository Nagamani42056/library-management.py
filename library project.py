class Book:

    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!")

    def view_books(self):

        if not self.books:
            print("No books available.")
            return

        for book in self.books:

            status = "Available" if book.available else "Issued"

            print("-" * 30)
            print("Book ID :", book.book_id)
            print("Title   :", book.title)
            print("Author  :", book.author)
            print("Status  :", status)

    def issue_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:

                if book.available:
                    book.available = False
                    print("Book issued successfully!")
                else:
                    print("Book already issued.")

                return

        print("Book not found.")

    def return_book(self, book_id):

        for book in self.books:

            if book.book_id == book_id:

                if not book.available:
                    book.available = True
                    print("Book returned successfully!")
                else:
                    print("Book was not issued.")

                return

        print("Book not found.")


library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        book = Book(book_id, title, author)
        library.add_book(book)

    elif choice == "2":
        library.view_books()

    elif choice == "3":

        book_id = int(input("Enter Book ID: "))
        library.issue_book(book_id)

    elif choice == "4":

        book_id = int(input("Enter Book ID: "))
        library.return_book(book_id)

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")