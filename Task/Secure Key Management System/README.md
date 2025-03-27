# 🔐 Secure Key Management and Encryption System

## 🚀 Overview
This project implements a **secure key management and encryption system** using **AES, RSA, and Diffie-Hellman key exchange**. It ensures confidentiality, integrity, and secure communication by providing functionalities for:

✅ **Centralized key distribution** for symmetric encryption (AES)  
✅ **Public Key Infrastructure (PKI)** for asymmetric encryption (RSA)  
✅ **Secure key exchange** using Diffie-Hellman  
✅ **Key revocation** to disable compromised keys  

---

## 📌 Features
- **🔑 Generate Symmetric Keys** (AES-based encryption)  
- **🔒 Encrypt & Decrypt Messages** using AES (CBC mode)  
- **🔑 Generate RSA Key Pairs** for secure communication  
- **📩 Encrypt & Decrypt Messages** using RSA keys  
- **🔗 Secure Key Exchange** using **Diffie-Hellman**  
- **❌ Key Revocation System** to prevent unauthorized access  

---

## 🛠️ Installation
### **Prerequisites**
Ensure you have **Python 3.x** installed.

### **Install Required Dependencies**
Run the following command:
```sh
pip install pycryptodome cryptography
```

### **Run the Script**
```sh
python script.py
```

---

## 📜 System Design & Implementation
### **1️⃣ Centralized Key Distribution for Symmetric Encryption**
🔹 AES keys are generated per user and securely stored.  
🔹 **CBC mode** is used for encryption to enhance security.  
🔹 Keys can be revoked to prevent further access.  

### **2️⃣ Public Key Infrastructure (PKI) for Asymmetric Encryption**
🔹 RSA key pairs (public/private) are generated per user.  
🔹 The **public key** is used for encryption, and the **private key** is used for decryption.  
🔹 This follows a **PKI model**, where public keys can be freely distributed while private keys remain protected.  

### **3️⃣ Secure Key Exchange Using Diffie-Hellman**
🔹 Users perform a **Diffie-Hellman key exchange** to establish a shared secret key.  
🔹 The key is derived securely using **HKDF (HMAC-based Key Derivation Function)**.  
🔹 This shared key can then be used for **secure encrypted communication**.  

### **4️⃣ Key Revocation System**
🔹 If a user's key is compromised, it can be **revoked immediately**.  
🔹 Once revoked, all encryption and decryption functionalities for that user are disabled.  
🔹 This prevents unauthorized use, enhancing security.  

---

## 🔄 Usage Guide
Run the script and choose an option from the menu:
```
1️⃣ Generate Symmetric Key
2️⃣ Encrypt & Decrypt Message (AES)
3️⃣ Generate RSA Keys
4️⃣ Encrypt & Decrypt Message (RSA)
5️⃣ Perform Diffie-Hellman Key Exchange
6️⃣ Revoke Key
7️⃣ Exit
```

---

## 📌 Example Workflow
### **🔐 AES Encryption/Decryption**
1️⃣ Generate a symmetric key for a user.  
2️⃣ Encrypt a message using **AES**.  
3️⃣ Decrypt the message using **AES**.  

### **🔑 RSA Encryption/Decryption**
1️⃣ Generate an **RSA key pair**.  
2️⃣ Encrypt a message using the **RSA public key**.  
3️⃣ Decrypt the message using the **RSA private key**.  

### **🔗 Diffie-Hellman Key Exchange**
1️⃣ Generate **private keys** for two users.  
2️⃣ Compute the **shared key** between them.  

### **❌ Key Revocation**
1️⃣ Revoke a user’s key to prevent unauthorized access.  
2️⃣ The user will no longer be able to encrypt or decrypt messages.  

---

## 🖥️ Google Colab Link
Run this project on **Google Colab** with the link below:  
[🔗 Run on Google Colab](https://colab.research.google.com/drive/1cReuiKP7dsJhN4pIQHX9X0VuyXSwdEBw?usp=sharing)  

---

## ⚠️ Security Considerations
🚨 **This implementation is for educational purposes and should not be used in production.**  

✔ **Use secure key storage mechanisms** instead of in-memory storage.  
✔ **Implement authentication & access control** to restrict unauthorized access.  
✔ **Enhance security** by using larger key sizes & additional integrity checks.  



