# 5. Create a class called `Person` with attributes `name` and `age`.
# Example:
# Create an instance of `Person` with the name 'Alice' and age 30.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def Display(self):
        print(self.name , self.age)

person = Person('Alice' , 30)
person.Display()
    
    
    