# Playfair Cipher Complexity

## **Encryption & Decryption Process**

### **Matrix Generation:**
- The Playfair cipher consists of a **5×5 matrix** containing **25 alphabet characters**.
- Unique characters from the key are inserted first, and the remaining letters are filled in.
- **Time Complexity:**
  - Since the matrix size is fixed, this operation takes **O(25) = O(1)** (constant time).

### **Pair Substitution (Bigram Encryption/Decryption):**
- Pairs of letters are encrypted using **row/column/rectangle rules**.
- **Finding positions of two characters in the matrix:** O(1) per pair.
- **Encrypting n characters requires:** O(n/2) = O(n).

## **Overall Complexity:**

\[
O(1) + O(n) = O(n)
\]

✅ **Playfair Cipher has a linear time complexity of O(n).**
