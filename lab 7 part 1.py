                                                                                                                               class Book:
    def _init_(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def _str_(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def _init_(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book added: {book}")

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
            for book in self.books:
                print(book)

    def search_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if not found_books:
            print(f"No books found with the title: {title}")
        else:
            print(f"Books found with the title '{title}':")
            for book in found_books:
                print(book)


# Example usage:
if _name_ == "_main_":
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "9780141182636")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0061120081")

    library.add_book(book1)
    library.add_book(book2)

    library.display_books()

    library.search_by_title("The Great Gatsby")                                                                                                                                                             

    