def main():
    print("Welcome to the calculator app")
    print("Here are he options: ")
    print("1. Add two numbers")
    print("2. Calculate area of circle")
    print("3. Solve 2nd order equation")

    option_selected = int(input("Enter the option you wish to do: "))
    if option_selected == 1:
        add_numbers()
    elif option_selected == 2:
        another_function()    


def add_numbers():
    x = int(input("Enter one number"))
    y = int(input("Enter another number"))

    result = x + y
    print("Result is: ", result)


if __name__ == "__main__": main()