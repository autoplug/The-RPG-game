class Book:
    title = ""
    author = ""
    year = 2000
    weight = 0

    def __init__(self, title, author, year, weight):
        self.title = title
        self.author = author
        self.year = year
        self.weight = weight

    def __str__(self):
        return self.title


class Library:
    books = []
    name = ""

    def __init__(self, name):
        self.name = name

    def add(self, book):
        self.books.append(book)

    def get_books_by_year(self, year):
        result = []
        for book in self.books:
            if book.year == year:
                result.append(book)
        return result

    def get_lightest(self):
        result = None
        for book in self.books:
            if not result or book.weight < result.weight:
                result = book
        return result

    def remove(self, title):
        index = -1
        for book_index in range(len(self.books)):
            if self.books[book_index].title == title:
                index = book_index
        if index != -1:
            self.books.pop(index)


library = Library("City Central")
library.add(Book("Life of A", "A", 2000, 8))
library.add(Book("Life of B", "B", 2000, 10))
library.add(Book("Life of C", "C", 2001, 12))
library.add(Book("Life of D", "D", 2002, 16))
print(len(library.get_books_by_year(2000)))  # should print: 2
print(library.get_lightest())  # should print: Life of A
library.remove("Life of A")
library.add(Book("Life of D", "D", 2002, 2))
print(len(library.get_books_by_year(2000)))  # should print: 1
print(library.get_lightest())  # should print: Life of D
