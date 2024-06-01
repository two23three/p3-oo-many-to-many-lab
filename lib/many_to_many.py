class Author:

    all = []

    def __init__(self, name):
        self.name = str(name)
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum([contract.royalties for contract in self.contracts()])


class Book:

    all = []

    def __init__(self, title):
        self.title = str(title)
        Book.all.append(self)
    
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]

class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception
        self._author = value

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception
        self._book = value

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception
        self._date = value

    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception
        self._royalties = value

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
        
# Creating instances of Author
author1 = Author("J.K. Rowling")
author2 = Author("George R.R. Martin")

# Creating instances of Book
book1 = Book("Harry Potter and the Philosopher's Stone")
book2 = Book("A Game of Thrones")
book3 = Book("Harry Potter and the Chamber of Secrets")

# Creating instances of Contract
contract1 = Contract(author1, book1, "1997-06-26", 50000)
contract2 = Contract(author2, book2, "1996-08-06", 60000)
contract3 = Contract(author1, book3, "1998-07-02", 55000)
contract4 = Contract(author2, book1, "2020-01-01", 7000) 

# Verify the instances and relationships
print("Authors:")
for author in Author.all:
    print(f"- {author.name}")

print("\nBooks:")
for book in Book.all:
    print(f"- {book.title}")

print("\nContracts:")
for contract in Contract.all:
    print(f"- Author: {contract.author.name}, Book: {contract.book.title}, Date: {contract.date}, Royalties: {contract.royalties}")

# Test Author methods
print("\nContracts for J.K. Rowling:")
for contract in author1.contracts():
    print(f"- {contract.book.title} on {contract.date} for {contract.royalties}")

print("\nBooks written by George R.R. Martin:")
for book in author2.books():
    print(f"- {book.title}")

print("\nTotal royalties for J.K. Rowling:")
print(author1.total_royalties())
