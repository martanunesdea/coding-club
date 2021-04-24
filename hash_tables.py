def main():
    newline = "\n"

    # Create a hash table using Python's dictionary
    items1 = dict( 
        {"key1": 1,
        "key2": 2,
        "key3": "three"})
    
    # Caution, items aren't necessarily saved in order
    print(items1)
    print(newline)
    # print(items1["key6"])   # exception error: key doesn't exist
       
    # Create a hash table dinamically
    items2 = {}             # creates an empty dictionary

    items2[1] = "one"     # initialise key/value pair
    items2["key2"] = 2
    items2["key3"] = 3
    #print(items2)
    print(newline)

    items2["key2"] = "two" 
    #print(items2)
    

    

    # Iteratre the keys and values in the dictionary
    for key, value in items2.items():
        print("Key: ", key, " value: ", value)


if __name__ == "__main__": main()