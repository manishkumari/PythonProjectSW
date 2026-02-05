import pytest
from Library import Book
from Library import Library
def test_book_borrow_success():
    book = Book("Clean Code", "Robert Cecil Martin")
    success = book.borrow()
    assert success is True
    assert book.available is False

def test_borrow_book_available():
    lib = Library()
    lib.add_book("Dune", "Frank Herbert")
    result = lib.borrow_book("Dune")
    assert result == True
    assert lib.books[0].available == False

def test_initialize_library():
    book = Book("Clean Code", "Robert Martin")
    assert book.title == "Clean Code"
    assert book.author == "Robert Martin"
    assert book.available is True

    def test_borrow_when_available(self):
        book1 = Book("1122", "George Orwell")
        available = book.borrow()
        self.assertTrue(available is True)
        self.assertFalse(book.available)

    def test_borrow_when_not_available(self):
        book2 = Book("ABC", "XYZ")
        book.borrow()
        available = book.borrow()
        self.assertFalse(available is False)
        self.assertFalse(book.available)

    def test_return_book(self):
        book3 = Book("Brave New World", "Aldous Huxley")
        book.borrow()
        book.return_book()
        self.assertTrue(book.available)