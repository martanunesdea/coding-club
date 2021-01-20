# Functions
# A tool to create blocks of code
# Which can be called separate to the remaining source file

# A function with 2 arguments, x is 1 by default
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


# A function with varying number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result 
 

newline = "\n"
print(newline)

print("2 to the power of 1: ", power(2))
print("2 to the power of 3: ", power(2,3))

print("Explicitly passing arguments: ", power(num=2, x=3))
print(newline)


print(multi_add(4, 5, 10, 4))

scale = multi_add(1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Result is ", scale)

