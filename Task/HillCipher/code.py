import numpy as np

def encrypt(plaintext,key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    if len(plaintext) % n != 0:
        plaintext += "X" * (n - len(plaintext) % n)

    vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""

    for i in range(0, len(vector), n):
        block = vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)
    return ciphertext

plaintext = input("Enter the text:")
key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
print("Encrypted:", encrypt(plaintext, key_matrix))

# plaintext = "SHORT"
# key_matrix = np.array([[7,8], [11,11]])
# print("Encrypted:", encrypt(plaintext, key_matrix))
