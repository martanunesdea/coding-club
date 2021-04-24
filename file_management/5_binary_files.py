def main():
    original = open("picture.jpg", "rb")
    copy = open("picture-copy.jpg", "wb")

    while True:
        buffer = original.read(10240)
        if buffer:
            copy.write(buffer) 
            print('.', end='', flush=True)
        else: break
    copy.close()
    original.close()
    print("\ndone.")


if __name__ == "__main__": 
    main()