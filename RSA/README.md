# 🔐 RSA Encryption and Decryption

## 📝 Description
This project demonstrates a simple implementation of the **RSA cryptographic algorithm** in Python. RSA is an **asymmetric encryption algorithm** that relies on a pair of keys—one public and one private—to securely encrypt and decrypt messages. It is widely used in secure communications, digital signatures, and data encryption.

## ⚙️ How It Works
### 1️⃣ Key Generation
- Select two prime numbers **p** and **q**.
- Compute **n** as the product of `p` and `q` → `n = p * q`.
- Compute **Euler's totient function** → `phi = (p-1) * (q-1)`.
- Choose an encryption key **e**, such that **e** is coprime with `phi`.
- Determine the decryption key **d**, which satisfies the equation `(d * e) % phi = 1`.

### 2️⃣ Encryption Process
- Convert the plaintext message into a numerical format.
- Compute the encrypted message using the formula:
  
  	`c = (msg ** e) % n`
  
  Here, `c` is the **ciphertext** (the encrypted version of the message).

### 3️⃣ Decryption Process
- Recover the original message by applying the decryption key **d**:
  
  	`d_msg = (c ** d) % n`
  
  This restores the plaintext message from the encrypted text.

## 🚀 Usage Guide
1. Open the provided **Google Colab** notebook and execute the script.
2. Enter values for **p**, **q**, and the message you want to encrypt.
3. The script will:
   - Compute encryption and decryption keys automatically.
   - Display the encrypted and decrypted message.

## 🔢 Example Execution
```plaintext
Enter the value of p: 7
Enter the value of q: 11
Enter a message: 5
Encrypted message: 26
Decrypted message: 5
```

## 🌍 Real-World Applications
✅ **Secure Communication** – Used in messaging apps, email encryption, and online transactions.
✅ **Digital Signatures** – Verifies the authenticity and integrity of digital documents.
✅ **Data Protection** – Ensures sensitive data is securely stored and transmitted.
✅ **Authentication Systems** – Used in login mechanisms and identity verification.

## 🔗 Google Colab Link
Click below to run the project in **Google Colab** and test RSA encryption & decryption yourself:

➡️ [Run on Google Colab](https://colab.research.google.com/drive/1ISkJDC55aUMiI6qJ3G_vo1KRyfHGdJp2?usp=sharing) 🚀
