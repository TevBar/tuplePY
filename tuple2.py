def add_book(library, book):
    """
    Adds a new book to the library if it doesn't already exist.

    Parameters:
        library (list): A list of tuples, each representing a book (title, author).
        book (tuple): A tuple containing the book's title and author.

    Returns:
        str: A message indicating the result of the operation.
    """
    if book in library:
        return f"The book '{book[0]}' by {book[1]} already exists in the library."
    else:
        library.append(book)
        return f"The book '{book[0]}' by {book[1]} has been added to the library."

# Existing library data
library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

# Adding new books
print(add_book(library, ("1984", "George Orwell")))  # Duplicate book
print(add_book(library, ("Fahrenheit 451", "Ray Bradbury")))  # New book
print(add_book(library, ("The Handmaid's Tale", "Margaret Atwood")))  # Another new book

# Printing updated library
print("\nUpdated Library:")
for i, (title, author) in enumerate(library, start=1):
    print(f"{i}. {title} by {author}")
