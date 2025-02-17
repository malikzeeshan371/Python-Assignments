# 8. Add a method `area` to the `Rectangle` class that returns the area of the rectangle.
# Example:
# If the rectangle has length 10 and width 5, calling `area` should return 50.

class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width 
        print(area)

rectangle = Rectangle(10 , 5)
rectangle.area()
        