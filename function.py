# # FUNCTIONS
# # def input():
# #     print('This is a function')

# # input()


# a = int(input('enter a number: '))
# b = int(input('enter a number: '))
# def add():
#     sum = a+b
#     print('Sum is: ', sum)

# add()


# def sub():
#     c = a-b
#     print('The difference is: ', c)

# sub()  


# def mul():
#     d = a*b
#     print('Product is: ',d)
    
# mul()


# def div():
#     if b != 0:
#         e = a/b
#         print('The quotient is: ',e)
    
#     else:
#         print('Error')

# div()


# def rem():
#     r = a % b
#     print('The remainder is: ', r)

# rem()

# def fd():
#     z = a // b
#     f = int(z)
#     print('The floor division is: ', z)

# fd()


# def cName(country = 'Nepal'):
#     # print(f'Hello, {country}')
#     # print('Hello, ', country)
#     print('Hello,'+ ' ' + country)

# cName('India')
# cName('USA')
# cName()
# cName('Canada')

def display_pattern(rows):
    for i in range(1, rows + 1):  # Loop through the number of rows
        print(" * " * i)          # Print '*' repeated 'i' times

# Call the function to display the pattern
display_pattern(5)

# N 
# N E 
# N E P
# N E P A
# N E P A L

def display_pattern(word):
    for i in range(1, len(word) + 1):
        print(word[:i])  # Print the first 'i' characters of the word

# Call the function with the word "NEPAL"
display_pattern("NEPAL")
