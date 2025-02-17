# 3. Create another class called `Dog` that inherits from the `Animal` class.
# Example:
# Create an instance of `Dog` with the name 'Buddy'.
class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name}"
    
dog = Dog("Buddy")
print(dog.speak())