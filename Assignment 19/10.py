# 10. Create a class called `Circle` with an attribute `radius`.
# Example:
# Create an instance of `Circle` with radius 7.
# Add a method `area` to the `Circle` class that returns the area of the circle (use 3.14 as the value of pi).
# Example:
# If the circle has a radius of 7, calling `area` should return approximately 153.86.


class Circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        pi = 3.14
        diameter =  self.radius * self.radius
        return pi*diameter

circle = Circle(7)
print(f"Area of circle is {circle.area()}")