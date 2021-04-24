def main():
    # Write a dictionary/hash table
    table = {0: "marta", 1: "oscar", 2: "john", 3: "peter"}

    # Want to save it to a file..
    f = open("table.txt", "w+") 
    for key, value in table.items():
        line = "Key: " + str(key) + "\tValue: " + value + "\n"
        print(line)
        f.write(line)

    f.close()


if __name__ == "__main__": main()