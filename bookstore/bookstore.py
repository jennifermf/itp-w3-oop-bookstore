class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def search_books(self, title = None, author = None):
        qlist = []
        for item in self.books:
            if item.author == author:
                qlist.append(item)
            elif item.title == title:
                qlist.append(item)
            elif title and item.title.lower().startswith(title.lower()):
                qlist.append(item)
            else:
                continue
        return qlist
    def get_books(self):
        return self.books

class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.bookinventory = []
    def get_books(self):
        return self.bookinventory

class Book(object):                 # this class works!
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.bookinventory.append(self)