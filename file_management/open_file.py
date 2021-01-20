# Open a file for writing 
f = open("textfile.txt", "w+")

# Open the file for appending text to the end
# f = open("textfile.txt", "a") # a is for appending content to file rather than overwriting

# write some lines of data to the file
for i in range(10):
    f.write("This is line " + str(i) + " \r\n")

f.close()

# Open the file and read the contents
f = open("textfile.txt", "r")
contents = f.read()
print(contents)

"""
# print by line
fl = f.readlines()
for x in fl:
    print(x)
"""