# Open existing file with "a" access for appending
def main():
    f = open("textfile.txt", "a")

    for i in range(10):
        f.write("A different line appended " + str(i))

    f.close()

if __name__ == "__main__":
    main()