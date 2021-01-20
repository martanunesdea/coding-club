# Functions
# A tool to create blocks of code
# Which can be called separate to the remaining source file

# A function without arguments
def func1():
    print("I am a simple function")
    print("hi")
    print("how are you")


# A function with 2 arguments
def func2(arg1, arg2):
    print("Arguments given: ", arg1, " ", arg2)


# A function with 1 argument, returns a variable
def cube(x):
    return x*x*x

# A function with 2 arguments, x is 1 by default
def power(base, exp = 1):
    result = 1
    for i in range(exp):
        result = result * base
    return result


# A function with varying number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result


newline = "\n"

#func1()


#func2(13, 20)
"""
print(newline)

cube(3)             # result is returned but not catching it
result = cube(3)    # result is caught but not printing it
print("3 cubed is ", result)

print("Printing result directly: ", cube(3) )

print("4 cubed is ", cube(4))
"""


print(newline)
print("2 to the power of 1: ", power(2))
print("2 to the power of 3: ", power(2,3))

print("Explicitly passing arguments: ", power(num=2, x=3))
print(newline)
"""

print(multi_add(4, 5, 10, 4))
scale = multi_add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Result is ", scale)
"""