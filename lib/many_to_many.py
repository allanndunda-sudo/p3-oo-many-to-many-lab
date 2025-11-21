class Author:
    all_authors = []
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self.name = name
        Author.all_authors.append(self)

    def __str__(self):
        return f"Author: {self.name}"

    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]   

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties) 
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    pass
    def __str__(self):
        return f"Author: {self.name}"


class Book:
    all_books = []
    def __init__(self, title):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self.title = title
        Book.all_books.append(self)
        pass
    def contracts(self):
        return [contract for contract in Contract.all_contracts if contract.book == self]
    def authors(self):
        return [contract.author for contract in self.contracts()]
    pass

    def __str__(self):
        return f"Book: {self.title}"


class Contract:
    all_contracts = []
    

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("book must be a Book instance")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, (int, float)) or isinstance(royalties, bool):
            raise Exception("royalties must be a number")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [c for c in cls.all_contracts if c.date == date]
    
    def __str__(self):
        return (f"Contract: {self.author.name} - {self.book.title} "
                f"on {self.date} for {self.royalties}%")
