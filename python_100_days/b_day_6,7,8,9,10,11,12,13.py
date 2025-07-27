a = 1 # Data type: int
print(a) # print the value of a

b = "Nitesh" # Data type: str
print(b) # print the value of b

c = True # Data type: bool
print(c) # print the value of c

d = None # Data type: NoneType
print(d) # print the value of d

e = complex(2, 3) # Data type: complex
print(e) # print the value of e

list = [1, 2, 3, 4, 5, [6, 7, 8],["Nitesh","Kumar","Singh"]] # Data type: list
print(list) # print the value of list : mutable (can be changed)

tuple = (1, 2, 3, 4, 5, [6, 7, 8],["Nitesh","Kumar","Singh"]) # Data type: tuple
print(tuple) # print the value of tuple : immutable (can't be changed)

dict1 = {"first": "Nitesh", "second": "Kumar", "third": "Singh"} # Data type: dict
print(dict1) # print the value of dict1 : key-value pairs

#everything is an object in python



print("\n\n")

#operators in python
# Arithmetic Operators
x = 10
y = 5
print("The value of ",x, "+", y, "is", x + y) # Addition
print("The value of ",x, "-", y, "is", x - y) # Subtraction
print("The value of ",x, "*", y, "is", x * y) # Multiplication
print("The value of ",x, "/", y, "is", x / y) # Division
print("The value of ",x, "//", y, "is", x // y) # Floor Division
print("The value of ",x, "%", y, "is", x % y) # Modulus
print("The value of ",x, "**", y, "is", x ** y) # Exponentiation



print("\n\n")

#Typecasting : It is the conversion of one data type to another
x = "10"
y = "5"
print(int(x)+int(y)) # explicit typecasting from str to int (doing by myself)

c = 1.9
d = 8
print(c+d) # implicit typecasting from int to float (done by python itself)



print("\n\n")

#User Input
a = input("Enter your name: ") # input function takes input from user
print("Hello", a) # print the value of a

a = (input("Enter a number: ")) 
b = (input("Enter another number: "))
print("Cocatenation of the two numbers is:", a + b) # concatenation of strings
print("The sum of the two numbers is:", int(a) + int(b)) # converting input to int for addition



print("\n\n")

#String Methods

apple = '''This is a multi-line string
that spans multiple lines.
It can be used to write longer text without using escape characters.'''
print(apple) # print the multi-line string

str1 = "Nitesh Jha" # Enclosed in double quotes : strings are immutable
print("The original string is: " + str1)
print(str1[0]) # Accessing the first character of the string
print(str1[0:5]) # Slicing the string from index 0 to 5
print(str1[0:-1]) # Slicing the string from index 0 to -1

for char in str1: # Iterating through each character in the string
    print(char, end=" \n") # Print each character with a newline

print("The length of the string is:", len(str1))
print("The string in uppercase is:", str1.upper())
print("The string in lowercase is:", str1.lower())
print("The string after replacing is:", str1.replace("Nitesh", "John"))

nm = "Harry"
print(nm[-4:-2]) # From [1:3]


name = "!!!Nitesh !!!!!!"
print(name.rstrip("!")) # Removing trailing '!' characters
print(name.lstrip("!")) # Removing leading '!' characters
print(name.strip("!")) # Removing leading and trailing '!' characters
print(name.split(" ")) # Splitting the string by space
print(name.split("!")) # Splitting the string by '!'

blogHeading = "intro to pyThon"
print(blogHeading.capitalize()) # Capitalizing the first letter of the string
print(blogHeading.center(50, "*")) # Centering the string with '*' padding
print(blogHeading.center(50)) # Centering the string
print(blogHeading.count("o")) # Counting occurrences of 'o' in the string
print(blogHeading.endswith("on")) # Checking if the string ends with 'on'
print(blogHeading.startswith("itro")) # Checking if the string starts with 'itro'
print(blogHeading.find("to")) # Finding the index of 'to' in the string
print(blogHeading.index("to")) # Finding the index of 'to' in the string (raises error if not found)
print(blogHeading.isalnum()) # Checking if the string is alphanumeric
blogHeading = "intro to pyThon 123"
print(blogHeading)
print(blogHeading.isalpha()) # Checking if the string contains only alphabetic characters
print(blogHeading.isdigit()) # Checking if the string contains only digits
blogHeading = "Intro to python"
print(blogHeading)
print(blogHeading.isascii()) # Checking if the string contains only ASCII characters
print(blogHeading.islower()) # Checking if the string is in lowercase
print(blogHeading.isupper()) # Checking if the string is in uppercase
print(blogHeading.isprintable()) # Checking if the string is printable
print(blogHeading.isspace()) # Checking if the string contains only whitespace  
print(blogHeading.title()) # Converting the string to title case
print(blogHeading.swapcase()) # Swapping the case of the string