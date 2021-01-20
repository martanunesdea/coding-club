# Conditionals
# Allows for decision making based on the values of our variables

def compare(x, y):
    if (x < y):
        st = " x is less than y"
    elif (x == y):
        st = " x is the same as y"
    else:
        st = "x is greater than y"
    
    print(st)

def main():
    x = input("Enter your first number of choice: ")
    y = input("Enter your second number of choice: ")
    compare(x, y)


if __name__ == "__main__":
    main()