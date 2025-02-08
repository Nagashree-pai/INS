# Hill Cipher Complexity

## **Encryption Process**

### **Key Matrix Setup:**
- The key is an **m×m matrix**.
- **Time Complexity:** O(m²) (since it involves filling in m² elements).

### **Matrix Multiplication (Key × Plaintext Vector):**
- Matrix-vector multiplication takes **O(m²)** operations per block.
- With **n** plaintext characters, the number of blocks is **O(n/m)**.
- **Total Complexity:**  
  \[
  O(m^2 \cdot n/m) = O(mn)
  \]

## **Decryption Process**

### **Matrix Inversion (Key Inversion):**
- Inverting an **m×m matrix** takes **O(m³)** using Gaussian elimination.
- The inverse is then multiplied with ciphertext vectors: **O(mn)**.

## **Overall Complexity:**

\[
O(m^3) + O(mn) = O(m^3 + mn)
\]

✅ **Hill Cipher has a complexity of O(m³ + mn), which is polynomial.**
