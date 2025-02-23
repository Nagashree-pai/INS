# 🔐 Vigenère Cipher - A Timeless Encryption Technique  

## 📜 Definition  

The **Vigenère Cipher** is a classic encryption technique that extends the **Caesar Cipher** by using a keyword to shift letters differently across the message. Developed in the **16th century**, it remained one of the strongest ciphers until the advent of modern cryptography!  

---

## ✨ Features  

✅ Encrypts and decrypts messages with a **keyword-based shifting** mechanism  
✅ Handles both **uppercase and lowercase letters**  
✅ Retains **non-alphabetic characters** (spaces, punctuation, numbers)  
✅ Simple yet **historically significant** encryption technique  

---

## 🚀 Usage  

### 🔹 Encryption  
1. Each letter in the plaintext is shifted based on a letter from the **repeating key**.  
2. The shift is determined by the **position of the key letter in the alphabet**.  
3. The result is a **ciphertext** that appears randomized and secure!  

### 🔹 Decryption  
1. The key is used to **reverse the shifts** applied during encryption.  
2. This restores the **original message**.  

---

## 🛠️ Example  

```plaintext
Input:
Plaintext: HELLO WORLD
Key: KEY

Output:
Ciphertext: RIJVS UYVJN

Input:
Ciphertext: RIJVS UYVJN
Key: KEY

Output:
Decrypted Text: HELLO WORLD
```

---

## 📋 Requirements  

- Python **3.x** installed  
- Basic knowledge of string manipulation in Python  

---

## ▶️ How to Run  

1️⃣ Save the script as `vigenere_cipher.py`  
2️⃣ Open a terminal and navigate to the script location  
3️⃣ Run the script using:  

   ```bash
   python vigenere_cipher.py
   ```

4️⃣ Enter your **plaintext and key** for encryption  
5️⃣ Enter the **ciphertext and key** to decrypt  

---

## 🌍 Applications  

🔹 **Secure Communications** – Used historically for military and diplomatic encryption  
🔹 **Puzzle & CTF Challenges** – Frequently appears in cybersecurity competitions  
🔹 **Steganography** – Can be combined with other techniques to hide messages  
🔹 **Educational Purposes** – Helps understand cryptographic principles  

---

 

