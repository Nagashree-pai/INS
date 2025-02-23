# 🔐 Feistel Cipher - A Simplified Implementation

## 📜 Introduction  
The **Feistel Cipher** is a symmetric encryption technique used in modern cryptographic algorithms like **DES (Data Encryption Standard)**. It splits the plaintext into two halves and processes them through multiple rounds of encryption using a key. This implementation showcases a **basic Feistel Cipher with two rounds** for educational purposes.

---

## ✨ Features  
✅ Converts plaintext into binary representation  
✅ Splits the binary into left and right halves  
✅ Uses a simple XOR and modular addition operation for encryption  
✅ Decrypts the ciphertext back to plaintext  
✅ Basic two-round Feistel structure

---

## 🛠️ Code Explanation  
### 🔹 Step 1: Convert Plaintext to Binary
- The input string is converted into an **8-bit binary format** using `ord()` and `format()` functions.

### 🔹 Step 2: Split into Left and Right Halves
- The binary string is divided into **left (L) and right (R) halves**.

### 🔹 Step 3: Key Conversion
- The encryption key is also converted into **binary format**.

### 🔹 Step 4: First Round of Encryption
- The **right half (R)** is added with the key (modular addition).
- The result is XORed with the **left half (L)**.
- The values of **L and R are swapped**.

### 🔹 Step 5: Second Round of Encryption
- The same process is repeated with the swapped values.
- This final output is the **ciphertext**.

### 🔹 Step 6: Decryption
- The process is **reversed**, applying the **same steps in reverse order** to retrieve the original plaintext.

---

## 🚀 Usage  
### 🔹 Installation
1️⃣ Open the [Google Colab link](https://colab.research.google.com/drive/1lJof-PZK8evqM1L15s5rcgbqStdLLOor?usp=sharing)  
2️⃣ Run the code cell and input the required text & key  
3️⃣ The encrypted and decrypted messages will be displayed  

### 🔹 Running the Script Locally
1️⃣ Save the script as `feistel_cipher.py`
2️⃣ Open a terminal and navigate to the script location
3️⃣ Run the script using:
   ```sh
   python feistel_cipher.py
   ```
4️⃣ Enter the **plaintext and key**
5️⃣ The **encrypted and decrypted text** will be displayed

---

## 📋 Example  
```sh
Enter a string: HELLO
Result (Binary): 0100100001000101010011000100110001001111
Enter a key: KEY
Ciphertext (Binary): 0110101101010101010011100101110001100011
Decrypted text: HELLO
```

---

## 🌍 Applications  
🔹 **Data Encryption** – Used in cryptographic algorithms like DES  
🔹 **Security & Authentication** – Basis for modern encryption techniques  
🔹 **Educational Use** – Helps understand Feistel network-based cryptography  

---

🔗 **Try the Code Now:** [Google Colab Link](https://colab.research.google.com/drive/1lJof-PZK8evqM1L15s5rcgbqStdLLOor?usp=sharing) 🚀


