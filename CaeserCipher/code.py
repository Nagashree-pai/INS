
def encrypt(plain_text, key):
    cipherText = ""
    for char in plain_text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            cipherText += chr((ord(char) - shift_base + key) % 26 + shift_base)
        else:
            cipherText += char
    return cipherText

# Decryption
def decrypt(text, key):
    pText = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            pText += chr((ord(char) - shift_base - key) % 26 + shift_base)
        else:
            pText += char
    return pText

plain_text=input("Enter the text to encrypt:")
key=int(input("Enter the key:"))
print("Cipher text:",encrypt(plain_text,key))
text=input("Enter the cipher text:")
key=int(input("Enter the key:"))
print("Plain text:",decrypt(text,key))
