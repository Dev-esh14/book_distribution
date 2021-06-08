"""
  Create a class Book with a parameterised constructor then takes name_of_book, author,
year_of_publish, price_of_book, no_of_copies_available. Create the following methods -
- order_book(no_of_books) : This method should return price of purchase, if no of
books is less than or equal to no_of_copies_available. Else, return “No stock”.
- add_quantity(is_admin, quantity): This method should add quantity of books (2nd
param) to existing no_of_copies_available if is_admin is True and return “Book
quantity updated as <<count>>” . If is_admin is False, return “Unauthorised” as
output.
Sample Input/Output:
book = Book(“Software Quality Assurance”, “Mr.Jochen”, 1994, 100, 50)

"""

class Book:
    def __init__(self,name_of_book,author,year_of_publish,price_of_book,no_of_copies_available):
        self.name_of_book=name_of_book
        self.author=author
        self.year_of_publish=year_of_publish
        self.price_of_book=price_of_book
        self.no_of_copies_available=no_of_copies_available

    def order_book(self,no_of_books):
        if(no_of_books<=self.no_of_copies_available):   
            print(self.price_of_book*no_of_books)
            self.no_of_copies_available-=no_of_books
        else:
            print("No stock")

    def add_quantity(self,is_admin,quantity):
        if(is_admin==True):
            self.no_of_copies_available += quantity
            print("Book quantity updated as",self.no_of_copies_available)
        else:
            print("Unauthorised")

book = Book("Software Quality Assurance", "Mr.Jochen", 1994, 100, 50)
book.order_book(10)
book.order_book(1000)
book.order_book(1)
book.order_book(43) 
book.add_quantity(False, 100)
book.add_quantity(True, 2)

"""
OUTPUT:
1000
No stock
100
No stock
Unauthorised
Book quantity updated as 41
"""