# 9. Add a method `perimeter` to the `Rectangle` class that returns the perimeter of the rectangle.
# Example:
# If the rectangle has length 10 and width 5, calling `perimeter` should return 30.

class Rectangle:
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def perimeter(self):
        perimeters = self.length + self.width
        print(2 * perimeters)

rectangle = Rectangle(10 , 5)
rectangle.perimeter()
