def main():
    # Open file with in "r" mode to READ the contents of the file
    f = open("textfile.txt", "r")

    # check if file can be read, if it cannot then no point in trying
    """
    if f.mode == "r": 
        contents = f.read()
        print(contents)
    
    """
    # read contents line by line
    lines = f.readlines()
    for x in lines:
        print(x)
    
    f.close()

if __name__ == "__main__":
    main()