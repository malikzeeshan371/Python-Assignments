# 1. Create a class called `Animal` with a single attribute `name`.
# Example:
# Create an instance/object of `Animal` with the name 'Dog'.

class Animal:
    def __init__(self , name):
        self.name = name

a1 = Animal('Dog')
print(a1.name)