#Create a class Book with members as bid, bname, price and author .
#By using Constructor method

class Book:
    count = 0
    
    def __init__(self,bid = 0,bname = "Unknown",price = 0.0,author = "Unknown"):
        self.bid = bid 
        self.bname = bname 
        self.price = price
        self.author = author
        Book.count += 1
     
    @staticmethod
    def showData(self):
        print("Total Books Created:", Book.count)

b1 = Book(101, "Python", 500, "Guido")
b2 = Book(102, "Java", 600, "James Gosling")

Book.showData()


