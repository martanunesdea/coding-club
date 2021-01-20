# Loops
# A helpful tool to iterate through repetitive steps
# For loops, while loops are the most common

def main():

    # use a for loop over a collection
    print("\nA for loop over a list \n")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for d in days:
        print(d)

    # use break and continue statements
    print("\nA for loop with conditionals \n")
    for x in range(5, 10):
        #if(x < 9): continue
        if(x > 7): 
            break
        else:
            print(x)

    # using the enumerate() function to get index
    print("\nEnumerating items\n")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    for i, d in enumerate(days):
        print(i, d)
    


if __name__ == "__main__":
    main()