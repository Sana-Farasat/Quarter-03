# Built-in module
import json
# Installed
from termcolor import colored

class BookCollection:
    """A class to manage a collection of books, allowing users to store and organize their reading materials"""

    def __init__(self):
        """Initialize a new book collection with an empty list and setup file storage"""
        self.book_list = []
        self.storage_file = "books_data.json"
        self.read_from_file()

    def read_from_file(self):
        """Load saved books from json file into memory.
        If the file doesn't exist or is corrupted, start with an empty collection."""
        try:
            with open(self.storage_file, "r") as file:
                self.book_list = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.book_list = []

    def save_to_file(self):
        """Store the current book collection to a json file for permanent storage"""
        with open(self.storage_file, "w") as file:
            json.dump(self.book_list, file, indent=4)

    def create_new_book(self):
        """Add a new book to the collection by gathering information from the user"""
        book_title = input(colored("Enter book title: ", "blue"))
        book_author = input(colored("Enter book author: ", "blue"))
        publication_year = int(input(colored("Enter publication year: ", "blue")))
        book_genre = input(colored("Enter book genre: ", "blue"))
        is_book_read = (
            input(colored("Have you read this book? (yes/no)", "blue")).strip().lower() == "yes"
        )

        new_book = {
            "title": book_title,
            "author": book_author,
            "year": publication_year,
            "genre": book_genre,
            "read": is_book_read,
        }

        self.book_list.append(new_book)
        self.save_to_file()
        print(colored("Book added successfully! \n" , "green"))

    def delete_book(self):
        """Remove a book from the collection using its title"""
        book_title = input(colored("Enter the title of the book to remove: ", "blue"))

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                self.book_list.remove(book)
                self.save_to_file()
                print(colored("Book removed successfully \n", "green"))
                return
        print(colored("Book not found!", "red"))

    def find_book(self):
        """Search for books in the collection by title or author name"""
        search_type = input(colored("Search by \n 1. Title \n 2. Author \n Enter your choice: ", "blue"))
        search_text = input(colored("Enter search term: ", "blue")).lower()

        found_books = [
            book
            for book in self.book_list
            if search_text in book["title"].lower() or search_text in book["author"].lower()
        ]

        if found_books:
            print(colored("Matching Books: ", "green"))
            for index, book in enumerate(found_books, 1):
                reading_status = "Read" if book["read"] else "Unread"
                print(colored(
                    f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}", "green"
                ))
        else:
            print(colored("No matching books found. \n", "red"))

    def update_book(self):
        """Modify the details of an existing book in the collection"""
        book_title = input(colored("Enter the title of the book you want to edit: ", "blue"))

        for book in self.book_list:
            if book["title"].lower() == book_title.lower():
                print(colored("Leave blank to keep an existing value", "green"))
                book["title"] = input(colored("New title ({book['title']}): ", "yellow")) or book["title"]
                book["author"] = input(colored(f"New author ({book['author']}): ", "yellow")) or book["author"]
                book["year"] = input(colored(f"New year ({book['year']}): ", "yellow")) or book["year"]
                book["genre"] = input(colored(f"New genre ({book['genre']}): ", "yellow")) or book["genre"]
                book["read"] = input(colored("Have you read this book? yes/no: ", "yellow")).strip().lower() == "yes"
                
                self.save_to_file()
                print(colored("Book updated successfully! \n", "green"))
                return
        
        print(colored("Book not found! \n","red"))

    def show_all_books(self):
        """Display all books in the collection with their details"""
        if not self.book_list:
            print(colored("Your collection is empty \n", "magenta"))
            return

        print(colored("Your Book Collection: ", "magenta"))
        for index, book in enumerate(self.book_list, 1):
            reading_status = "Read" if book["read"] else "Unread"
            print(colored(
                f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {reading_status}", "green"
            ))
        print()

    def show_reading_progress(self):
        """Calculate and display statistics about your reading progress"""
        total_books = len(self.book_list)
        completed_books = sum(1 for book in self.book_list if book["read"])
        completion_rate = (
            (completed_books / total_books * 100) if total_books > 0 else 0
        )

        print(colored(f"Total books in collection: {total_books}", "yellow"))
        print(colored(f"Reading progress: {completion_rate:.2f}% \n", "yellow"))

    def start_application(self):
        """Run the main application loop with a user-friendly interface"""
        while True:
           print(colored("\t\t📚 Welcome to Your Book Collection Manager! 📚", "green"))
           print(colored("\n1. Add a new book", "yellow"))
           print(colored("2. Remove a book", "yellow"))
           print(colored("3. Search for books", "yellow"))
           print(colored("4. Update book details", "yellow"))
           print(colored("5. View all books", "yellow"))
           print(colored("6. View reading progress", "yellow"))
           print(colored("7. Exit", "yellow"))
           user_choice = input(colored("\n Please choose an option (1-7): ", "blue"))

           if user_choice == "1":
                self.create_new_book()
           elif user_choice == "2":
                self.delete_book()
           elif user_choice == "3":
                self.find_book()
           elif user_choice == "4":
                self.update_book()
           elif user_choice == "5":
                self.show_all_books()
           elif user_choice == "6":
                self.show_reading_progress()
           elif user_choice == "7":
                self.save_to_file()
                print(colored("Thank you for using Book Collection Manager. Goodbye!", "green"))
                break
           else:
                print(colored("Invalid choice. Please try again.\n", "red"))

if __name__ == "__main__":
    book_manager = BookCollection()
    book_manager.start_application()
