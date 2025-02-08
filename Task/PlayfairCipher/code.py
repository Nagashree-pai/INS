
# Create a matrix
def create_matrix(key):
    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix=[]
    key="".join(dict.fromkeys(key.upper().replace("J","I")+alphabet))
    for i in range(0,25,5):
        matrix.append(list(key[i:i+5]))
    return matrix

# Find the position
def find_position(matrix,char):
    for row in range (5):
        for col in range (5):
            if matrix[row][col]==char:
                return row,col
# Encryption
def encrypt(ptext,key):
    matrix=create_matrix(key)
    ptext=ptext.upper().replace("J","I").replace(" ","")
    #Check for odd length text
    if len(ptext) %2 !=0:
        ptext+="X"

    ciphertext=""
    for i in range(0,len(ptext),2):
        a,b=ptext[i],ptext[i+1]
        row1,col1=find_position(matrix,a)
        row2,col2=find_position(matrix,b)

        if row1==row2:
            ciphertext+=matrix[row1][(col1+1)%5]+matrix[row2][(col2+1)%5]
        elif col1==col2:
            ciphertext+=matrix[(row1+1)%5][col1]+matrix[(row2+1)%5][col2]
        else:
            ciphertext+=matrix[row1][col2]+matrix[row2][col1]
    return ciphertext

# Decryption
def decrypt(text,key):
    matrix=create_matrix(key)
    text=text.upper().replace("J","I").replace(" ","")


    plaintext=""
    for i in range(0,len(text),2):
        a,b=text[i],text[i+1]
        row1,col1=find_position(matrix,a)
        row2,col2=find_position(matrix,b)

        if row1==row2:
            plaintext+=matrix[row1][(col1-1)%5]+matrix[row2][(col2-1)%5]
        elif col1==col2:
            plaintext+=matrix[(row1-1)%5][col1]+matrix[(row2-1)%5][col2]
        else:
            plaintext+=matrix[row1][col2]+matrix[row2][col1]
    return plaintext

# Inputs
# ptext="instruments"
# key="monarchy"
ptext=input("Enter the plain text:")
key=input("Enter the key:")
print("Encripted message:",encrypt(ptext,key))
text=input("Enter the cipher text:")
key=input("Enter the key:")
print("Encripted message:",decrypt(text,key))
