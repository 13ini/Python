# # Parent class
# class Animal:
#     def speak(self):
#         return "The animal makes a sound."

# # Child classes with specific implementations
# class Dog(Animal):
#     def speak(self):
#         return "The dog barks."

# class Cat(Animal):
#     def speak(self):
#         return "The cat meows."

# # Demonstrating polymorphism
# animals = [Animal(), Dog(), Cat()]

# for animal in animals:
#     print(animal.speak())

class Parent:
    def __init__(self, name):
        self.name = name

    def activity(self):
        print(f"{self.name} is taking care of the family.")

class Grandparent:
    def __init__(self, name):
        self.name = name

    def activity(self):
        print(f"{self.name} is sharing wisdom and stories.")

class Child:
    def __init__(self, name):
        self.name = name

    def activity(self):
        print(f"{self.name} is playing and learning.")

# Create instances of each class
parent = Parent("John")
grandparent = Grandparent("Margaret")
child = Child("Emily")

# Demonstrating polymorphism
for person in (parent, grandparent, child):
    person.activity()

