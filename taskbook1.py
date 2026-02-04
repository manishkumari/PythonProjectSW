class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if not self.available:
            return False
        self.available = False
        return True

    def return_book(self):
        self.available = True
def test_initialize_library():
    book = Book("Clean Code", "Robert Cecil Martin")
    assert book.title == "Clean Code"
    assert book.author == "Robert Cecil Martin"
    assert book.available is True

    def test_borrow_when_available(self):
        book1 = Book("1984", "George Orwell")
        available = book.borrow()
        self.assertTrue(available is True)
        self.assertFalse(book.available)

    def test_borrow_when_not_available(self):
        book2 = Book("The Hobbit", "J.R.R. Tolkien")
        book.borrow()
        available = book.borrow()
        self.assertFalse(available is False)
        self.assertFalse(book.available)

    def test_return_book(self):
        book = Book("Brave New World", "Aldous Huxley")
        book.borrow()
        book.return_book()
        self.assertTrue(book.available)