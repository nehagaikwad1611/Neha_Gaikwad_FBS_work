#Create a class Book with members as bid, bname, price and author .
#By using destructor method

class Book:
    def __init__(self,bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        print (f"[Book Created]{self.bname}")

    
    def __del__(self):
        print(f"[Object is destroyed]{self.bname}")

b1 = Book(101, "Python", 500, "Guido")
del b1