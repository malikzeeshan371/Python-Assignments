# 4. Add a method `bark` to the `Dog` class that prints "Woof!".
# Example:
# If the instance is a dog, calling the method `bark` should output "Woof!".


class Dog:
    def __init__(self,speak):
        self.speak = speak

    def bark(self):
        print(f"{self.speak}")

dog = Dog("Woof!")
dog.bark()

        