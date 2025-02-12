import datetime

# Define a class for books in the library.
class Book:
    def __init__(self, title, author, copies):
        """
        Initialize a book instance with a title, author, and number of copies.
        :param title: str, the title of the book
        :param author: str, the author's name
        :param copies: int, the number of available copies
        """
        self.title = title
        self.author = author
        self.copies = copies
        self.borrowed_by = {}  # Dictionary to track who borrowed the book.

    def copy_in_library(self):
        """
        Check if there is at least one copy of the book available in the library.
        :return: bool, True if copies > 0, otherwise False
        """
        return self.copies > 0

    def borrow(self, user_name):
        """
        Allow a user to borrow a book, and track the borrower's name and due date.
        :param user_name: str, the name of the borrower
        :return: bool, True if the borrowing was successful, False otherwise
        """
        if self.copy_in_library():
            self.copies -= 1
            due_date = datetime.date.today() + datetime.timedelta(days=14)  # 2 weeks due date
            self.borrowed_by[user_name] = due_date
            return True, due_date
        return False, None

    def return_book(self, user_name):
        """
        Allow a user to return a book and check if it's overdue.
        :param user_name: str, the name of the borrower
        :return: str, message about the return status
        """
        if user_name in self.borrowed_by:
            due_date = self.borrowed_by[user_name]
            overdue = datetime.date.today() > due_date
            if overdue:
                self.copies += 1
                return f"Book returned late. It was due on {due_date}. You owe a late fee."
            else:
                self.copies += 1
                del self.borrowed_by[user_name]
                return f"Book returned on time. It was due on {due_date}."
        else:
            return "This book was not borrowed by the user."


# A global dictionary to store books by their titles.
library = {}

# A global dictionary to track registered users
users = {}

# Function to populate the library with initial data.
def populate_library():
    """
    Populate the library dictionary with a set of predefined books.
    """
    library["Atomic Habits"] = Book("Atomic Habits", "James Clear", 5)
    library["Knotebook"] = Book("Knotebook", "Toby", 6)
    library["Brave New World"] = Book("Brave New World", "Aldous Huxley", 7)
    library["The Twilight Saga"] = Book("The Twilight Saga", "M.K", 7)


# Function to list all books in the library.
def list_books():
    """
    Display all books in the library, including their authors and number of copies.
    """
    print(f"{'Title':<30}{'Author':<20}{'Copies':<10}")
    print("-" * 60)
    for title, book in library.items():
        print(f"{title:<30}{book.author:<20}{book.copies:<10}")


# Function to list all available books with copies > 0.
def list_available_books():
    """
    Display only the books that have at least one copy available in the library.
    """
    print(f"{'Title':<30}{'Author':<20}{'Copies':<10}")
    print("-" * 60)
    for title, book in library.items():
        if book.copy_in_library():
            print(f"{title:<30}{book.author:<20}{book.copies:<10}")


# Function to register a new user.
def register_user():
    """
    Register a new user for the library.
    """
    username = input("Enter your name to register: ").strip()
    if username not in users:
        users[username] = {}
        print(f"User {username} registered successfully!")
    else:
        print(f"User {username} already exists.")


# Function to borrow a book from the library.
def borrow_a_book(title, user_name):
    """
    Borrow a book by reducing its available copy count by one.
    :param title: str, the title of the book to borrow
    :param user_name: str, the name of the borrower
    """
    if title in library:
        book = library[title]
        success, due_date = book.borrow(user_name)
        if success:
            print(f"\nYou have borrowed '{title}' by {book.author}. Due date: {due_date}")
        else:
            print("\nThat book is not available.")
    else:
        print("\nThat book does not exist in the library.")


# Function to return a borrowed book to the library.
def return_a_book(title, user_name):
    """
    Return a borrowed book by increasing its available copy count by one.
    :param title: str, the title of the book to return
    :param user_name: str, the name of the borrower
    """
    if title in library:
        book = library[title]
        message = book.return_book(user_name)
        print(message)
    else:
        print("\nThat book does not exist in the library.")


# Function to display the main menu and allow the user to interact with the library system.
def main_menu():
    """
    Display the main menu and allow the user to interact with the library system.
    """
    populate_library()

    while True:
        print("\nLibrary Menu:")
        print("1. List All Books")
        print("2. List Available Books")
        print("3. Register User")
        print("4. Borrow a Book")
        print("5. Return a Book")
        print("6. Quit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            list_books()
        elif choice == '2':
            list_available_books()
        elif choice == '3':
            register_user()
        elif choice == '4':
            user_name = input("Enter your name: ").strip()
            title = input("Enter the title of the book to borrow: ").strip()
            borrow_a_book(title, user_name)
        elif choice == '5':
            user_name = input("Enter your name: ").strip()
            title = input("Enter the title of the book to return: ").strip()
            return_a_book(title, user_name)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main_menu()
