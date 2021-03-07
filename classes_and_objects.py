# Basic class syntax
class Solution(object):
    def __init__(self) -> None:
        super().__init__()
        ...


# objects

class myClass:
    variable = 'hello'

    def function(self):
        print("This is a message inside class.")

myObject = myClass()

# Accessing object variable
x = myObject.variable
print(x)
# this prints "Hello" to console.
