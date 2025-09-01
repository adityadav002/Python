def show_menu():
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. Show All Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"\"{self.title}\" by \"{self.author}\" is [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Book '{title}' added to library")

    def show_books(self):
        if not self.books:
            print("Library is empty!!!")
        else:
            for i, book in enumerate(self.books, 1):
                print(f"{i}. {book}")

    def borrow_book(self, title):
        for book in self.books:
            if (title.lower() == book.title.lower()):
                if book.is_borrowed:
                    print("Book is already borrowed")
                else:
                    book.is_borrowed = True
                    print(f"You borrowed '{book.title}'")
            return
        print("Book not found")

    def return_book(self, title):
        for book in self.books:
            if (title.lower() == book.title.lower()):
                if not book.is_borrowed:
                    print("This book was not borrowed")
                else:
                    book.is_borrowed = False
                    print(f"You returned '{book.title}'")
            return
        print("Book not found")

library = Library()

while True:
    show_menu()
    choice = input("Choose an option (1-5): ").strip()

    if (choice == '1'):
        title = input("Enter the book title: ")
        author = input("Enter the author name: ")
        library.add_book(title, author)

    elif(choice == '2'):
        library.show_books()

    elif(choice == '3'):
        title = input("Enter the title of the book to borrow: ")
        library.borrow_book(title)

    elif(choice == '4'):
        title = input("Enter the title of the book to borrow: ")
        library.return_book(title)
    
    elif(choice == '5'):
        print("Goodbye: visit again!!!")
        break

    else:
        print("Invalid chioce: choose b/w (1-5)")