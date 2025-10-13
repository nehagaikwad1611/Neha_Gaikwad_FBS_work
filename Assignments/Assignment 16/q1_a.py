#Create a class Book with members as bid, bname, price and author .
#By using Constructor method

class Book:
    def __init__(self, bid, bname, price, author):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def showData(self):
        data = f'ID: {self.bid}\nNAME: {self.bname}\nPRICE: {self.price}\nAUTHOR: {self.author}'
        return data


b1 = Book(101, "Python", 500, "Guido")
print(b1.showData())
print("Book Object created With constructor.")
