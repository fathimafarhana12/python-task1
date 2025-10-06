class Book:
    def __init__(self,title):  
        self.title=title
        self.is_borrowed=False

class Member:
    def __init__(self,name):  
        self.name=name

    def borrow_book(self,library,title):
        if title in library.books and not library.books[title].is_borrowed:
            library.books[title].is_borrowed=True
            print(f"{self.name} borrowed '{title}'")  
        else:
            print(f"Sorry, '{title}' not available")  

    def return_book(self,library,title):
        if title in library.books and library.books[title].is_borrowed:
            library.books[title].is_borrowed=False
            print(f"{self.name} returned '{title}'") 
        else:
            print(f"{self.name} cannot return '{title}'") 


class Library:
    def __init__(self): 
        self.books = {}

    def add_book(self, title):
        self.books[title] = Book(title)

    def show_books(self):
        print("Available book:")
        for title, book in self.books.items():
            if not book.is_borrowed:
                print(title)
        print()

library=Library()
library.add_book("IKIGAI")
member1=Member("Farhana")
member2=Member("Sumi")

library.show_books()
member1.borrow_book(library, "IKIGAI")  
member2.borrow_book(library, "IKIGAI") 


