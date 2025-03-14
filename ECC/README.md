# 🔐 Elliptic Curve Cryptography (ECC) Key Exchange

## 📜 Definition
**Elliptic Curve Cryptography (ECC)** is a modern public-key cryptography method that provides strong security with smaller key sizes compared to traditional RSA. This implementation demonstrates how two parties can securely exchange keys using ECC and **Elliptic Curve Diffie-Hellman (ECDH)**.

---

## 🧠 How It Works
1. **Choose an Elliptic Curve** - We use `brainpoolP256r1` from the `tinyec` registry.
2. **Generate Private & Public Keys** - Each party selects a private key and derives a public key.
3. **Compute Encryption Key**:
   - A temporary ciphertext public key is generated.
   - The shared encryption key is computed using ECC point multiplication.
4. **Exchange Public Keys & Compute Shared Secret** - The receiver can derive the same shared encryption key.

Since both parties compute the same shared key, they can securely communicate! 🔑

---

## 🚀 Usage
This Python program simulates an **ECC key exchange** between a sender and a receiver.

### 📌 Example Output
```
Sender's private key:  0x4a3b5c...
Sender's public key:  0x9f8a7d...1

Sender's ciphertext public key:  0x2f6c9e...0
Sender's encryption key:  0x3e4b2d...1

Receiver's private key:  0x5d2a9c...
Receiver's public key:  0x8e7d6b...0

Receiver's ciphertext public key:  0x1c4e5a...1
Receiver encryption key:  0x3e4b2d...1
```
✅ **Both encryption keys match!**

---

## 🎯 How to Run
### 🔗 Run in Google Colab:
[Click Here to Run in Colab 🚀](https://colab.research.google.com/drive/1WBAMVfxx-ZAMREenEsttqkoRROvvDC7f?usp=sharing)

### 🏃 Run Locally:
1. Install dependencies:
   ```bash
   pip install tinyec
   ```
2. Copy the script into a file (e.g., `ecc_key_exchange.py`)
3. Open a terminal and run:
   ```bash
   python ecc_key_exchange.py
   ```
4. Observe the generated keys and shared encryption key.

---

## 🎯 Applications
- **Secure Communication** 🔒 (e.g., Messaging Apps, VPNs)
- **Blockchain & Cryptocurrency Transactions** 🪙
- **TLS & Secure Web Browsing** 🌐
- **IoT Security & Lightweight Encryption** 🔗

---

## 📌 Notes & Improvements
✅ The `secrets` module ensures cryptographic randomness.

✅ ECC offers better security with smaller keys than RSA (e.g., 256-bit ECC ≈ 3072-bit RSA).

✅ Experiment with different ECC curves for optimized security!

---

### 🔥 Stay Secure with ECC! 🚀


