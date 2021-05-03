string = 'Hello World'

print(len(string))
# this will print lenght of characters in string

print(string.index('o'))
# That prints out 4, because the location of the first occurrence of the letter "o" is 4 characters 
# away from the first character. Notice how there are actually two o's in the phrase - this method 
# only recognizes the first.

# But why didn't it print out 5? Isn't "o" the fifth character in the string? To make things more 
# simple, Python (and most other programming languages) start things at 0 instead of 1. So the index of "o" is 4.

# String formatting
# Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a 
# set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal 
# text together with "argument specifiers", special symbols like "%s" and "%d".

name= 'Jhon'
print("Hello, %s!" % name)
# This prints out - Hello, Jhon!

# to use two or more arguments, use tuple (parentheses)
name = "Axay"
age = 26
print("%s is %d years old." % (name, age))
# Axay is 26 years old.

# Any object which is not a string can be formatted using the %s operator as well. The string which returns 
# from the "repr" method of that object is formatted as the string. For example:

# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

'''
Here are some basic argument specifiers you should know:

%s - String (or any object with a string representation, like numbers)

%d - Integers

%f - Floating point numbers

%.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

%x/%X - Integers in hex representation (lowercase/uppercase)
'''