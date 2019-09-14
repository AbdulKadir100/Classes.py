class Book:
    def __init__(self):
        title = ""
        publisher = ""
        price = 0
    def set(self,title,publisher,price):
        self.title = title
        self.publisher = publisher
        self.price = price
    def display(self):
        print("Title is: ",self.title)
        print("Publisher is: ",self.publisher)
        print("Price is: ",self.price)

B1 = Book()
B1.set("OOPs with java","Dreamtech Press",480)
B1.display()
