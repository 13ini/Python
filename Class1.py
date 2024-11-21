# name= input("enter you name:")
# print ("your name is" , name)
# age= input("enter your age:")
# print ("ypur age is", age)


print('Hello, I am a student at "Softwarica"')
print("It's too cold today")

#its single line comment

"""
this is multi line comment
"""
#Different types variable
name = "Bini"        # String
age = 19              # Integer
height = 5.8          # Float
is_active = True      # Boolean

# Print variables directly
print(name)           # Output: Alice
print(age)            # Output: 30
print(height)         # Output: 5.8


#Checking the types
a = 10
b = 20.40
c = "hello"

print(type(a))  # Output: <class 'int'>
print(type(b))  # Output: <class 'float'>
print(type(c))  # Output: <class 'str'>

#Printing both single and double quote
print ('''Hello! Welcome to "Pytshon". It's so awesome''')

#WAP to print maximum number between two number
# Input: Two numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print("The maximum number is:", a)
else:
    print("The maximum number is:", b)

#WAP to print minimum among three numbers.
# Input: Three numbers
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

# Using conditional statements to find the minimum
if a <= b and a <= c:
    print("The minimum number is:", a)
elif b <= a and b <= c:
    print("The minimum number is:", b)
else:
    print("The minimum number is:", c)

#WAP to print even numbers from 1 to 100.
print([i for i in range(1, 101) if i %2==0])
       
#WAP tp print your name 10 times.
name = "BINI"
print((name + "\n") * 10)

#WAP to print odd numbers from 100 to 50.
print(list(range(99, 49, -2)))

#WAP to print prepare result sheet
name = str(input("Enter your name: "))
roll_no = int(input("Enter your roll no: "))
marks = int(input("Enter your marks: "))
print('Name: ', name)
print('Roll No: ', roll_no)
if marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks >= 60:
    print("Grade: D")

elif marks >= 50:
    print("Grade: E")

else:
    print("Grade: Fail")