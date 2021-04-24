from cryptography.fernet import Fernet

## Generating key and saving it for later
key = Fernet.generate_key()
print(key)
# encode() will convert string to bytes
message = "my deep dark secret".encode()

## Encrypt message
f = Fernet(key)
encrypted = f.encrypt(message)
print("Encrypted secret: ", encrypted)

## Decrypt message
decrypted = f.decrypt(encrypted)

original_message = decrypted.decode()
print("Decrypted secret: ", original_message)