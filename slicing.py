#string slicing

#slice the given string into different formats

txt="hello world"
# print(txt[0:5])  # Output: hello
# print(txt[6:])   # Output: world
# print(txt[-5:])  # Output: world
# print(txt[:-6])  # Output: hello
# print(txt[::2])  # Output: hlowrd
# print(txt[::-1]) # Output: dlrow olleh
# print(txt[:5])   # Output: hello
# print(txt[6:])   # Output: world
#slice the given string into different format.
txt="hello world"
print(txt[0])
print(txt[-3])

# First 5 characters
print(txt[:5])  

# Characters from index 6 to the end
print(txt[6:])  

# Characters from index 3 to 7
print(txt[3:8]) 

# Every second character
print(txt[::2])  

# Reverse the string
print(txt[::-1]) 

# Split into words
words = txt.split(' ')
print(words)  

# Slice from the second last character to the end
print(txt[-5:])  

# Slice from the start to the second last character
print(txt[:-6])



#string in python
# Convert "softwarica" into uppercase
word = "softwarica"
uppercase = word.upper()
print(uppercase)  

# Display "SOFTwaRica" into samllcase using different string methods.
#Using lower method
word = "SOFTwaRica"
lowercase = word.lower()
print(lowercase)  

word= "SOFTwaRica"
lowercase= word.casefold()
print(lowercase)  


# Replace the letter 'h' with letter 't' from the word "hello"
word = "hello"
modified = word.replace('h', 't')
print(modified) 

# Rempove leading and traning sapce from the string "  Softwarica College  "
word = "  Softwarica College  "
cleaned = word.strip()
print(cleaned) 

# Split the string "Hello,Softwarica,College"
word = "Hello,Softwarica,College"
split = word.split(',')
print(split)


# shortform
# Convert "softwarica" into uppercase
print("softwarica".upper())  # Output: SOFTWARICA

# Display "SOFTwaRica" in lowercase using different methods
print("SOFTwaRica".lower())      # Output: softwarica (using lower())
print("SOFTwaRica".casefold())   # Output: softwarica (using casefold())

# Replace the letter 'h' with 't' in "hello"
print("hello".replace('h', 'T'))  # Output: tello

# Remove leading and trailing spaces from "  Softwarica College  "
print("  Softwarica College  ".strip())  # Output: Softwarica College

# Split the string "Hello,Softwarica,College"
print("Hello,Softwarica,College".split(","))  # Output: ['Hello', 'Softwarica', 'College']

# Check if the word "best" is present in "Honesty is the best policy"
print("best" in "Honesty is the best policy")  # Output: True

# Check if the word "worst" is present in "Honesty is the best policy"
print("worst" in "Honesty is the best policy")  # Output: False


#Print the number after inserting leading 6 zeroes to the number "5" using string function.
number = "5"
formatted= number.zfill(7)  
print(formatted)

# count the number of times the text "python" is repeated in the following string.
# "Hello, its awemosone to learn python. python is great"
text = "Hello, its awesome to learn python. python is great"
count_python = text.count("python")
print(count_python)  # Output: 2

