def encrypt(plaintext, key):
    key = key.upper()
    ciphertext = ""
    key_index = 0
    for c in plaintext.upper():
        if c.isalpha():
            shift = ord(key[key_index]) - ord('A')
            ciphertext += chr((ord(c) - ord('A') + shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        
        else:
            ciphertext += c
    
    return ciphertext

def decrypt(ctext, key):
    key = key.upper()
    text = ""
    key_index = 0
    for c in ctext.upper():
        if c.isalpha():
            shift = ord(key[key_index]) - ord('A')
            text += chr((ord(c) - ord('A') - shift) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        
        else:
            text += c
    
    return text

plaintext=input("Enter the text:")
key=input("Enter the key:")
print("Ciphertext:",encrypt(plaintext,key))
ctext=input("Enter the ciphertext:")
print("Ciphertext:",decrypt(ctext,key))
