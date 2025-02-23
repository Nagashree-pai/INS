# 🔐 Hill Cipher - Matrix-Based Encryption  

## 📝 Definition  

The **Hill Cipher** is a **polygraphic substitution cipher** that encrypts messages using **matrix multiplication** over a **modular arithmetic system**. It was **invented by Lester S. Hill in 1929** and is one of the earliest ciphers to use **linear algebra** in cryptography!  

---

## ✨ Features  

✅ Uses **matrix-based encryption** for stronger security  
✅ Encrypts multiple letters **simultaneously**  
✅ Requires an **invertible key matrix** for decryption  
✅ Resistant to frequency analysis attacks compared to simple substitution ciphers  

---

## 🚀 Usage  

### 🔹 Encryption  
1. Convert the plaintext into **numerical values** (A = 0, B = 1, ..., Z = 25).  
2. Break the message into **blocks** matching the size of the **key matrix**.  
3. Multiply each block with the **key matrix**, apply **mod 26**, and convert back to letters.  

### 🔹 Decryption  
1. Compute the **modular inverse** of the key matrix.  
2. Multiply the ciphertext blocks with the **inverse key matrix** and apply **mod 26**.  
3. Convert the resulting numbers back to letters.  

---

## 🛠️ Example  

```plaintext
Input:
Plaintext: ACT
Key Matrix: [[6, 24, 1], [13, 16, 10], [20, 17, 15]]

Output:
Ciphertext: POH

Input:
Ciphertext: POH
Key Matrix: [[6, 24, 1], [13, 16, 10], [20, 17, 15]]

Output:
Decrypted Text: ACT
```

---

## 📋 Requirements  

- Python **3.x** installed  
- NumPy (`pip install numpy`)  
- SymPy (`pip install sympy`)  

---

## ▶️ How to Run  

1⃣ Save the script as `hill_cipher.py`  
2⃣ Open a terminal and navigate to the script location  
3⃣ Run the script using:  

   ```bash
   python hill_cipher.py
   ```

4⃣ Enter your **plaintext and key matrix** for encryption  
5⃣ Enter the **ciphertext and key matrix** for decryption  

---

## 🌍 Applications  

🔹 **Secure Communications** – Used for encrypting military and confidential messages  
🔹 **Cybersecurity Challenges** – Common in cryptanalysis and hacking competitions  
🔹 **Mathematical Research** – Demonstrates the power of **modular arithmetic**  
🔹 **Educational Purposes** – Helps students learn about **linear algebra in cryptography**  

---

## 📚 Run on Google Colab  

You can also run this code on **Google Colab** by clicking the link below:  

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1e60y6w4N4I1UJglSTGaaZPXCQ4MBh2jr?usp=sharing)

