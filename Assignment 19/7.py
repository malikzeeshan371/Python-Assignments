# 7. Create a class called `Rectangle` with attributes `length` and `width`.
# Example:
# Create an instance of `Rectangle` with length 10 and width 5.

class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def attributes(self):
        print(f"The length is {self.length} and width is {self.width}")
        

rectangle = Rectangle(10 , 5)
rectangle.attributes()