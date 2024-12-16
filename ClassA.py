# class A35:
#     x=10
#     y=20
#     name="abc"

# p1=A35
# #creating objects
# print(p1.x)
# print(p1.y)
# print(p1.name)

# #Syntax
# #class classname:
#     #prgram part:
# class A35:
#     x=10
#     y=20
#     name="abc"

# p1=A35
# #creating objects
# print(p1.x)
# print(p1.y)
# print(p1.name)




# class PersonalDetails:
#     name="bini"
#     age=19
#     gender="Female"
#     gmail="bini@gmail.com"
#     number="123456789"

# p1=PersonalDetails 
# print("My name is:", p1.name)
# print("My age is:", p1.age)
# print("Gender is:", p1.gender)
# print("My Email is :", p1.gmail)
# print("Phone   :", p1.number)

#create a class named person, use the __init__() function to assing values for name qand age and so on

#Create a class named Person using init function to assign the values for name and age.
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("Bini",16)

# print("My name is ",p1.name,".")
# print("My age is",p1.age,"years old.")

class Person:
    def __init__(self, name, age, gender, email, phone):
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone = phone

# Creating an instance of the Person class
person1 = Person(name="Bini", age=19, gender="Female", email="bini@gmail.com", phone="123456789")

# Accessing and printing the details
print ("Name:", person1.name)
print("Age:", person1.age)
print("Gender:", person1.gender)
print("Email:", person1.email)
print ("Phone:", person1.phone)
