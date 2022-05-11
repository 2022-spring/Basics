# This is my first file, this line is comment line for me to put some description
# comment line will always be ignored by execution

# Variables - storage while your program runs, during execution time
message = "hello world!"
# message is the name of the variable
# "hello world!" is the value , '=' sign is setting a value to a variable
print(message)
print()

# Naming rules: dont start with numbers, no spaces
# Best practice (PEP): better use lower, better short brief, better give meaningful name
# https://peps.python.org/pep-0001/

message_text = "avoid spaces in the name of the variables"
msg = 'this means message, it is acceptable name'
m = 'this is message text, not a good name, it might confuse you when you want to use this'
n = 'something to save, not a good name.'
my_neighbours_first_name_and_last_name = "john doe"
# print(my_neighbours_first_name_and_last_nam)

# shortcuts to know:
# ctrl/cmd + d - duplicates the line, copy the current line and past to next line
# ctrl + y - deletes the line (first time pycharm asks to select the option)
# ctrl + / - to comment/uncomment the line
# ctrl + s - save the file
print(message_text)
print(message_text)
print(message_text)
print(message_text)
# print(note) program does not know this variable yet, so we can not print it here

# Data types:
# primitive data: string (text), num (int, float, double), boolean (True/False), None
msg = "I am a string data type"
note = 'oh I am also a string data type'
num = 456
price = 99.99
result = True
truth = False
something_else = None

print(msg, note, something_else, num, price, something_else, truth, result)
print(note)

note = 'I am a updated value of the note!!!'
print(msg, note, something_else, num, price, something_else, truth, result)
print(note)

# String, What we can do with string variable: we can change the key cases using python functions for string variables
print(note.title())
print(note.upper())
print(note.lower())

print("####################### 03/31/2022 ##################")
# 2-1: Simple Message:
# short keys: ctrl + alt + L - automatically formats the current file
message = 'My name is Svetlana.'
print(message)
print(message)
message = 'Hi everyone!'  # reset the value of message variable
print(message)
print(message)

# Data types: String - text (word, latter, long paragraph ..), it is covered by 'string' or "string"
# some useful functions(methods) that are builtin and come with python
# What is functions? example here is print() function
print('hello\n', 'hi\n', 2)  # at the end of print there is always newline character(enter)
print('\t\t\t\tola\n', '\t\t\t\t\t\t\t\toley\n', 3)

print(" ########## string functions ###########")
print(message.upper())
first_name = 'john'
last_name = 'doe'
print(first_name.title() + " " + last_name.upper())  # concatenation

full_name = first_name.title() + "\t" + last_name.upper()
print(full_name)
print(first_name, last_name)

# Concatenation using fstring
fullname = f"Full name of the used: {first_name.title()} {last_name.upper()}."
print(fullname)
variableName = f"adding 23 to 50 is: {23 + 50}"
print(variableName)
location = '   \t\t\tbrookl    yn\n '
print(f"My location is :{location}.")
print(f"My location is :  {location.strip()}.")  # this function removes the whitespaces
print(f"My location is :{location}.")

# 2-4. Name Cases: Store a person’s name in a variable, and then print that person’s
# name in lowercase, uppercase, and titlecase.
fullname = f"Full name of the used: {first_name.title()} {last_name.upper()}."

# HW: 2-3, 2-5, 2-6, 2-7

#################   variables 04/03/2022 #########
num1 = 21
num2 = 5
num3 = 30

# operations
print(f"addition: {num1 + num2}")  # 26
print(f"subtraction: {num1 - num2}")  # 16
print(f"multiplication: {num1 * num2}")  # 105
print(f"division: {num1 / num2}")  # 4.2

print(f"exponent: {3 ** 2}")  # 9
print(f"modulo: {num1 % num2}")  # 1 (c)

# if result is 0 then it is EVEN number, if result is 1 then ODD number
print(f"modulo: {num1 % 2}")
# print("modulo: " + str(num1 % 2))
print(f"modulo: {num3 % 2}")

print(f"floor division: {num1 // num2}")  # 4 (b) | 21 = 5*4 + 1 >> num1 = num2*b + c

# numbers: integers, floats(double)
# using numbers with strings
age = 25  # int
age2 = "35"  # string

print("Hey I am " + str(age + 5))
print("my brother is " + age2 + " years old.")
print("my brother is " + str(int(age2) + 10) + " years old.")
print(f"my brother is {int(age2) + 10} years old.")
# Builtin functions to remember:
# int(string) : convert number or string  to an integer , returns 0 if it is not convertible
# str(object)
print(int(num1 / num2))

### Exercise: 2-9. Favorite Number: Store your favorite number in a variable.
# Then, using that variable, create a message that reveals your favorite number.
# Print that message.
num1 = 0
message = ""
# print message with fstring and with regular concatenation (use str() or int() functions)
