class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def ShowBook(self):
        print("Book Details:")
        print(f"ID: {self.bid}")
        print(f"Name: {self.bname}")
        print(f"Price: {self.price}")
        print(f"Author: {self.author}")

b1 = Book(103, "AI Fundamentals", 500, "Russell")
b1.ShowBook()
