from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method

    def common_behavior(self):
        print("All animals need food to survive.")  # Concrete method

# Concrete class
class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Using the classes
dog = Dog()
dog.sound()  # Output: Bark
dog.common_behavior()  # Output: All animals need food to survive.

cat = Cat()
cat.sound()  # Output: Meow
cat.common_behavior()  # Output: All animals need food to survive.

# Uncommenting the following line will raise an error
# because abstract classes cannot be instantiated:
# animal = Animal()