def main():
    # two parameters: filaname, and type of access
    # function returns and we store the file object in "f"
    f = open("textfile.txt", "w") 

    for i in range(10):
        f.write("This is  " + str(i) + "\n")

    f.close()

if __name__ == "__main__":
    main()