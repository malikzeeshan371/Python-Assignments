# 6. Add a method `greet` to the `Person` class that prints "Hello, my name is [name] and I am [age] years old."
# Example: If the instance has the name 'Alice' and age 30, calling `greet` should print "Hello, my name is Alice and
# I am 30 years old."

class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello my name is {self.name} and i am {self.age} years old ")


person = Person('Alice' , 30)
person.greet()
