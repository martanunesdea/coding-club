# Conditionals
# Allows for decision making based on the values of our variables

def main():
    x = 1000
    y = 10

    if (x < y):
        st = " x is less than y"
    elif (x == y):
        st = " x is the same as y"
    else:
        st = "x is greater than y"
    
    print(st)

    print("\nAlternatively:...")
    # python's more specific if/else
    
    statement = "x is less than y" if (x<y) else "x is greater than or the same as"
    print(statement)


if __name__ == "__main__":
    main()