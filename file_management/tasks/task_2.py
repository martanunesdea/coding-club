# Open file named "exam_results.txt"
# Extract data

# Group students into those who passed, and those who failed

# Print results OR 
# Write two files, one with those who passed, and one with those who

# Calculate % of students of passed

# hint 
#aline.find('F') != -1 --> F


def main():
    # two parameters: filaname, and type of access
    # function returns and we store the file object in "f"
    f = open("exam_results.txt", "r") 

    lines = f.readlines()
    for x in lines:
        if x.find('F'):
            print("failed")
        else:
            print("passed")

    f.close()

if __name__ == "__main__":
    main()