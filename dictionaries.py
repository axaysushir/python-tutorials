# A dictionary is a data type similar to arrays, but works with keys and values instead of indexes. 
# Each value stored in a dictionary can be accessed using a key, which is any type of object 
# (a string, a number, a list, etc.) instead of using its index to address it.

# For example, a database of phone numbers could be stored using a dictionary like this:

contacts = {}
contacts["John"] = 938477566
contacts["Jack"] = 938377264
contacts["Jill"] = 947662781
print(contacts)

# Dictionaries can be initialized by with this notations also it also called object in other programming languages
# :
contacts = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(contacts)

# Iterating over dictionaries
# Dictionaries can be iterated over, just like a list. However, a dictionary, unlike a list, 
# does not keep the order of the values stored in it. To iterate over key value pairs, use the following syntax:

contacts = {"John" : 938477566,"Jack" : 938377264,"Jill" : 947662781}
for name, number in contacts.items():
    print("Phone number of %s is %d" % (name, number))


# removing value form object
contacts = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

del contacts["John"]
print(contacts)

# or we can use pop() function to remove value from this object
contacts = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}

contacts.pop("John") # pop() will remove jhon from list and return other value
print(contacts)