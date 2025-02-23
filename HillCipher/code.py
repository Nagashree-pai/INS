import numpy as np

def mod_inverse_matrix(matrix, modulus):
    """Finds the modular inverse of a 2x2 matrix under a given modulus."""
    det = int(round(np.linalg.det(matrix)))  # Compute determinant
    det %= modulus  # Ensure positive determinant

    # Find modular inverse of the determinant
    det_inv = None
    for i in range(modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break

    if det_inv is None:
        raise ValueError("Matrix is not invertible under mod 26")

    # Calculate adjugate matrix
    adjugate = np.array([[matrix[1, 1], -matrix[0, 1]],
                         [-matrix[1, 0], matrix[0, 0]]])

    adjugate = (adjugate + modulus) % modulus  # Handle negative numbers

    # Calculate inverse matrix
    inverse_matrix = (det_inv * adjugate) % modulus
    inverse_matrix = inverse_matrix.astype(int)  # Convert to integers

    return inverse_matrix

def hill_cipher_encrypt(plaintext, key_matrix):
    """Encrypts the plaintext using the Hill Cipher with a 2x2 key matrix."""
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")

    # Pad plaintext with "X" if necessary
    while len(plaintext) % n != 0:
        plaintext += "X"

    plaintext_vector = [ord(char) - ord('A') for char in plaintext]
    ciphertext = ""

    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        result = np.dot(key_matrix, block) % 26
        ciphertext += "".join(chr(num + ord('A')) for num in result)

    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    """Decrypts the ciphertext using the inverse of the key matrix."""
    n = len(key_matrix)
    inverse_key_matrix = mod_inverse_matrix(key_matrix, 26)

    # Convert ciphertext to uppercase
    ciphertext = ciphertext.upper().replace(" ", "")
    ciphertext_vector = [ord(char) - ord('A') for char in ciphertext]
    plaintext = ""

    for i in range(0, len(ciphertext_vector), n):
        block = ciphertext_vector[i:i + n]
        result = np.dot(inverse_key_matrix, block)
        result = (result + 26) % 26  # Handle negative values
        plaintext += "".join(chr(num + ord('A')) for num in result)

    return plaintext

# Example usage
plaintext = input("Enter the text: ")  # Example: attack
key_matrix = np.array([[3, 3], [2, 5]])  # 2x2 key matrix

# Encrypt
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print("Encrypted:", ciphertext)

# Decrypt
ctext = input("Enter the ciphertext: ")  # Example: FRFMKC
decrypted_text = hill_cipher_decrypt(ctext, key_matrix)
print("Decrypted:", decrypted_text)
