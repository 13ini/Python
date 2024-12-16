#SYNTAX
# class ParentClass:
#     #parent class methods and attributes
#     pass

# class ChildClass(ParentClass):
#     #child class inherits from parentclass
#     pass
# Parent Class
# class Student:
#     def __init__(self, name, student_id):
#         self.name = name
#         self.student_id = student_id

#     def display(self):
#         return f"{self.name} is from Softwarica"

# # Child Class
# class Bini(Student):
#     def display(self):
#         return f"{self.name} is from Ethical 35A"

# # Using classes
# b = Bini("Bini", "12345")  
# print(b.display())

#SINGLE INHERITANCE

# Parent Class
# class Student:
#     def __init__(self, name):
#         self.name = name

#     def display(self):
#         return f"{self.name}"

# # Child Class
# class class1(Student):
#     def display(self):
#         return f"Bini is {self.name} "

# # Using classes
#  b = class1("from ethical")
# print(b.display())


#SINGLE INHERITANCE
# Parent Class
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"This car is a {self.brand} {self.model}."

# Child Class
class SportsCar(Car):
    def display(self):
        return f"This sports car is a {self.brand} {self.model} - built for speed!"

# Using classes
car = Car("Toyota", "Corolla")
sports_car = SportsCar("Ferrari", "488 Spider")

print(car.display())
print(sports_car.display())



