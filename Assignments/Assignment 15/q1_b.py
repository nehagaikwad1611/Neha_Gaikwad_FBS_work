class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print(f"Book object with ID {self.bid} destroyed.")


b1 = Book(102, "Data Structures", 400, "Tanenbaum")
del b1
