from cryptography.fernet import Fernet
 
# Saving the key in a separate file for later usage
file = open('key.key', 'rb')  # Open the file as wb to write bytes
key = file.read()  # The key is type bytes still
file.close()

# Open the file to encrypt
f = open('test.txt.encrypted', 'rb')
data = f.read()

# Encrypt data
fernet = Fernet(key)
decrypted = fernet.decrypt(data)
print(decrypted)

# Write the encrypted file
f = open('test.txt.decrypted', 'wb')
f.write(decrypted)
f.close()