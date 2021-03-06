# Basic class syntax
class Solution(object):
    def __init__(self) -> None:
        super().__init__()
        ...


# objects

class myClass:
    variable = 'hello'
    name = "Jhon"
    email = "jhon@email.com"
    address = "Bangalore"
    phone = "+919123456789"

    def function(self):
        print("This is a message inside class.")

myObject = myClass()

# Accessing object variable
x = myObject.variable
print(x)
# this prints "Hello" to console.

y = myObject.name
print(y) # this prints "Jhon" to console.

z = [myObject.name, myObject.email, myObject.address, myObject.phone]
print(z)
# ['Jhon', 'jhon@email.com', 'Bangalore', '+919123456789']
