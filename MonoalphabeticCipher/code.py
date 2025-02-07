
p = 'abcdefghijklmnopqrstuvwxyz'
ch = 'QWERTYUIOPASDFGHJKLZXCVBNM'

# Encryption
def encrypt(text):
    encrypted_text = ''
    for char in text:
        if char in p:
            encrypted_text += ch[p.index(char)]
        else:
            encrypted_text += char

    return encrypted_text

# Decryption
def decrypt(text):
    decrypted_text = ''
    for char in text:
        if char in ch:
            decrypted_text += p[ch.index(char)]
        else:
            decrypted_text += char

    return decrypted_text

message = input("ENTER THE MESSAGE TO ENCRYPT: ").lower()
eText = encrypt(message)
print("Encrypted message:", eText)
message = input("ENTER THE MESSAGE TO DECRYPT: ").upper()
dText = decrypt(message)
print("Decrypted message:", dText)
