# Functions
# What are Functions?
# Functions are a convenient way to divide your code into useful blocks, allowing us to order our code, make it more readable, reuse it and save some time. Also functions are a key way to define interfaces so programmers can share their code.

# How do you write functions in Python?
# As we have seen on previous tutorials, Python makes use of blocks.

# A block is a area of code of written in the format of:

# Functions in python are defined using the block keyword "def", followed with the function's name as the block's name. For example:

def my_function():
    print('Hello From My Function!')

# Functions may also receive arguments (variables passed from the caller to the function). For example:

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))


# Functions may return a value to the caller, using the keyword- 'return'
def sum_two_numbers(a, b):
    return a + b

# we call this function here to do some task
print(sum_two_numbers(2, 5))
# this return result 7


# TODO: How do we call Function in python

# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)

def multiply_two_numbers(a, b):
    return a * b

# function for find fibonaci series of nth number
def fibonac(n):
    if n == 1 or n == 2:
        res =  1
    else:
        res = fibonac(n-1) + fibonac(n-2)
    return res

fibonac(8)

# memoization
def fib(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n ==1 or n==2:
        res = 1
    else:
        res = fib(n-1, memo) + fib(n-2, memo)
    memo[n] = res
    return res 

def fib_memo(n):
    memo = [None] * (n+1)
    return fib(n, memo)