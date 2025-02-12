

# Library System for Borrowing Books

This example explains the implementation of a **Library System** where users can list books, check available books, borrow and return books. The system stores books using a class and a global dictionary. [Python File Here](library-management-system.py)

---

## **Code Breakdown**

### **1. Class Definition: Book**

We define a class `Book` to represent books in the library. Each book has the following attributes:

- **title**: The title of the book.
- **author**: The name of the author.
- **copies**: The number of copies available in the library.

The class also has a method to check whether a book is available in the library (i.e., if there are copies left).

#### Code:
```python
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

    def copy_in_library(self):
        """
        Check if there is at least one copy of the book available in the library.
        :return: bool, True if copies > 0, otherwise False
        """
        return self.copies > 0
```

### **2. Global Dictionary: Library**

We use a global dictionary called `library` to store books, where each book's title is the key, and the value is the book instance.

#### Code:
```python
library = {}
```

### **3. Function to Populate the Library**

The `populate_library` function adds a set of predefined books to the library. Each book is added to the dictionary with its title as the key.

#### Code:
```python
def populate_library():
    """
    Populate the library dictionary with a set of predefined books.
    """
    library["Atomic Habits"] = Book("Atomic Habits", "James Clear", 5)
    library["Knotebook"] = Book("Knotebook", "Toby", 6)
    library["Brave New World"] = Book("Brave New World", "Aldous Huxley", 7)
    library["The Twilight Saga"] = Book("The Twilight Saga", "M.K", 7)
```

### **4. Function to List All Books**

The `list_books` function displays all books in the library, including their title, author, and number of copies.

#### Code:
```python
def list_books():
    """
    Display all books in the library, including their authors and number of copies.
    """
    print(f"{'Title':<30}{'Author':<20}{'Copies':<10}")
    print("-" * 60)
    for title, book in library.items():
        print(f"{title:<30}{book.author:<20}{book.copies:<10}")
```

### **5. Function to List Available Books**

The `list_available_books` function filters the books in the library that have at least one copy available. It displays only those books where `book.copy_in_library()` returns `True`.

#### Code:
```python
def list_available_books():
    """
    Display only the books that have at least one copy available in the library.
    """
    print(f"{'Title':<30}{'Author':<20}{'Copies':<10}")
    print("-" * 60)
    for title, book in library.items():
        if book.copy_in_library():
            print(f"{title:<30}{book.author:<20}{book.copies:<10}")
```

### **6. Function to Borrow a Book**

The `borrow_a_book` function reduces the number of copies of the specified book by one when it is borrowed. It checks if the book exists in the library and if it is available.

#### Code:
```python
def borrow_a_book(title):
    """
    Borrow a book by reducing its available copy count by one.
    :param title: str, the title of the book to borrow
    """
    if title in library and library[title].copy_in_library():
        library[title].copies -= 1
        print(f"\nYou have borrowed '{title}' by {library[title].author}.")
    else:
        print("\nThat book is not available or does not exist.")
```

### **7. Function to Return a Book**

The `return_a_book` function increases the number of copies of a specified book by one when it is returned.

#### Code:
```python
def return_a_book(title):
    """
    Return a borrowed book by increasing its available copy count by one.
    :param title: str, the title of the book to return
    """
    if title in library:
        library[title].copies += 1
        print(f"\nYou have returned '{title}' by {library[title].author}.")
    else:
        print("\nThat book does not exist in the library.")
```

### **8. Main Menu**

The `main_menu` function displays a simple text-based interface allowing users to:

- List all books
- List available books
- Borrow a book
- Return a book
- Quit the application

The program loops indefinitely, offering these options until the user selects "Quit".

#### Code:
```python
def main_menu():
    """
    Display the main menu and allow the user to interact with the library system.
    """
    populate_library()

    while True:
        print("\nLibrary Menu:")
        print("1. List All Books")
        print("2. List Available Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Quit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            list_books()
        elif choice == '2':
            list_available_books()
        elif choice == '3':
            title = input("Enter the title of the book to borrow: ").strip()
            borrow_a_book(title)
        elif choice == '4':
            title = input("Enter the title of the book to return: ").strip()
            return_a_book(title)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```

### **9. Program Execution**

The program is started by calling the `main_menu` function inside the `if __name__ == "__main__":` block. This ensures the program only runs when executed directly.

#### Code:
```python
if __name__ == "__main__":
    main_menu()
```

---

## **Enhancements and Possible Improvements**

- **Data Persistence**: Currently, the library data is lost when the program ends. You could improve this by saving the library data to a file and loading it on startup.
- **Input Validation**: Further validation of user input could be added to ensure the program handles unexpected input gracefully.
- **Book Search**: A feature to search for books by title or author could be added for easier navigation of the library.
- **GUI**: Consider creating a graphical user interface (GUI) for more user-friendly interaction.

---

## **Final Thoughts**

This simple library system demonstrates how object-oriented programming (OOP) concepts can be applied to a real-world scenario. It is extendable, allowing additional features like book reservations, fines, or integration with an online catalog.
