class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

b1 = Book(101, "Python Basics", 350, "Guido")
print("Book object created successfully using constructor.")
