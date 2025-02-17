
# 2. Add a method `speak` to the `Animal` class that prints "The [name] says hello!".
# Example:
# If the instance has the name 'Dog', the output should be "The Dog says hello!"

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(f"The {self.name} says hello!")

dog = Animal("Dog")
dog.speak()