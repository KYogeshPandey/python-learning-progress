# class LibraryManagementSystem:
#     def __init__(self):
#         self.books = []
#         self.members = []
#         self.borrowed_books = {}

#     def add_book(self, title, author):
#         book = {'title': title, 'author': author}
#         self.books.append(book)

#     def register_member(self, name):
#         member = {'name': name}
#         self.members.append(member)

#     def borrow_book(self, member_name, book_title):
#         if member_name not in [member['name'] for member in self.members]:
#             print(f"Member '{member_name}' is not registered.")
#             return

#         if book_title not in [book['title'] for book in self.books]:
#             print(f"Book '{book_title}' is not available.")
#             return

#         if book_title in self.borrowed_books:
#             print(f"Book '{book_title}' is already borrowed.")
#             return

#         self.borrowed_books[book_title] = member_name
#         print(f"'{book_title}' has been borrowed by '{member_name}'.")

#     def return_book(self, book_title):
#         if book_title not in self.borrowed_books:
#             print(f"Book '{book_title}' was not borrowed.")
#             return

#         member_name = self.borrowed_books.pop(book_title)
#         print(f"'{book_title}' has been returned by '{member_name}'.")


class Library:
    def __init__(self):
        self.noBooks = 0
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        self.noBooks = len(self.books)

    def showInfo(self):
        print(f"the library has {self.noBooks} books and the books are")
        for book in self.books:
            print(book)


l1 = Library()
l1.add_book("Harry potter")
l1.add_book("The lord of the rings")
l1.showInfo()