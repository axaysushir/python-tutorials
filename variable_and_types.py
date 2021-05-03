# Variable and Data types
# Python is completely object oriented, and not "statically typed". You do 
# not need to declare variables before using them, or declare their type. 
# Every variable in Python is an object.

# This tutorial will go over a few basic types of variables.

# Numbers
# Python supports two types of numbers - integers(whole numbers) and floating 
# point numbers(decimals). (It also supports complex numbers, which will not be explained in this tutorial).

myInteger = 2 # myInteger is called variable & its value is int 2.

print(myInteger)

# TO definded floating point numbers you may use following approach
myfloat = 7.0
myfloat = 1.12345
print(myfloat)
myfloat = float(7)
print(myfloat)


# Strings in Python
# Strings are defined either with a single quote or a double quotes.
# Here string "This is your first string in python" is assigned to variable called myString.
# we can any numbers, strings to our variables in python.
myString = "This is your first string in Python"
print(myString)
# This is Spana's first string in Python

myvar = 'You can use single and double quotes to declare strings'

# Now we reassign myStrign variable
myString = "Axay doesn't know how to code in Python..."
print(myString)
# Axay doesn't know how to code in Python...


# There are additional variations on defining strings that make it easier to include 
# things such as carriage returns, backslashes and Unicode characters. These are beyond 
# the scope of this tutorial, but are covered in the Python documentation.

# Simple operators can be executed on numbers and strings:
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

# Assignments can be done on more than one variable "simultaneously" on the same line like this
a, b = 3, 4 
isha, nisha, tanisha = "Testing Engineer", "Software developer", "Product Manager"

# Mixing operators between numbers and strings is not supported:
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)

# Advanced variables in python
myObject = {} # this is empty object assigned to variable myObject
myArray = [] # this is empty array assigned to variable myArray, then we use it later to store value in that array

myArray.append([1, 2, 3, 'a', 'b', 'c']) # append only take single argument at a time
print(myArray)
# [[1, 2, 3, 'a', 'b', 'c']]