# Playfair Cipher Implementation
def create_matrix(key):
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix=[]
    key="".join(dict.fromkeys(key.upper().replace("J","I")+alphabet))
    for i in range(0,25,5):
        matrix.append(list(key[i:i+5]))
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col

def playfair_encrypt(text, key):
    matrix = create_matrix(key)
    text = text.upper().replace("J", "I").replace(" ", "")

    # Ensure even-length text
    if len(text) % 2 != 0:
        text += "X"

    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row → Shift right
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column → Shift down
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle → Swap columns
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

    return ciphertext

# Corrected Rail Fence Cipher (Zig-Zag Transposition)
def rail_fence_encrypt(text, rails):
    if rails == 1:
        return text  # No transposition needed for a single rail

    # Create a rail pattern
    fence = [''] * rails
    rail, direction = 0, 1

    for char in text:
        fence[rail] += char
        rail += direction
        if rail == 0 or rail == rails - 1:  # Change direction at ends
            direction *= -1

    return ''.join(fence)  # Read row-wise to get the ciphertext

# Hybrid Encryption Function
def hybrid_encrypt(plaintext, key, rails):
    playfair_encrypted = playfair_encrypt(plaintext, key)
    final_ciphertext = rail_fence_encrypt(playfair_encrypted, rails)
    return final_ciphertext

# Taking Inputs
ptext = input("Enter the plain text: ")
key = input("Enter the Playfair key: ")

# Ensuring valid rail input
while True:
    try:
        rails = int(input("Enter the number of rails for Rail Fence Cipher: "))
        if rails < 2:
            print("Rails should be at least 2. Try again.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Perform Hybrid Encryption
encrypted_text = hybrid_encrypt(ptext, key, rails)
print("Final Encrypted Message:", encrypted_text)
