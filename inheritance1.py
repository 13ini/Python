# class walk:
#     def walk(self):
#         return"This animal can walk."
    
# class Swimmer:
#     def swim(self):
#         return "This animal can swim."
    
# class Duck(walk, Swimmer):
#     def speak(self):
#         return "The ducks quacks."
    
# duck = Duck()
# print(duck.speak())
# print(duck.walk())
# print(duck.swim())

class Person:
    def __init__(self, name):
        self.name = name
        

    def fun1(self):
        return f"Name: {self.name}"
        
    
class Man(Person):
    def __init__(self, name, age, gender):
        super().__init__(name)
        self.age = age
        self.gender = gender

    def fun2(self):
        info = super().fun1()
        return f"{info} \nAge: {self.age} \nGender: {self.gender}"
    
class He(Man):
    def __init__(self, name, age, gender, height):
        super().__init__(name, age, gender)
        self.height = height

    def fun3(self):
        info = super().fun2()
        return f"{info} \nHeight: {self.height}cm"
    
naam = He('John', 21, 'Male', 180)
print(naam.fun3())