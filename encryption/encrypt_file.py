from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Saving the key in a separate file for later usage
file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()

# Open the file to encrypt
f = open('test.txt', 'rb')
data = f.read()

# Encrypt data
fernet = Fernet(key)
encrypted = fernet.encrypt(data)

# Write the encrypted file
f = open('test.txt.encrypted', 'wb')
f.write(encrypted)
f.close()