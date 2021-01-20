# Loops
# A helpful tool to iterate through repetitive steps
# For loops, while loops are the most common
def main():

    # define a while loop
    print("\nA while loop: \n")

    counter = 0
    while(counter < 10):
        print(counter) # key part of the code block
        counter = counter + 1  # update counter

    # define a for loop
    print("\nA for loop: \n")
    for x in range(1,6,2):
        print(x)        

    # use a for loop over a collection
    print("\nA for loop over a list \n")    
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for day in days:
        print(day)



if __name__ == "__main__":
    main()