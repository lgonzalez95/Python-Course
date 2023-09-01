class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def print_details(self):
        print('Book title: ', self.title)
        print('Book author: ',  self.author)
        print('Book price: ', self.price)


b = Book('Learn Python', 'Juanito', 100)
b.print_details()
