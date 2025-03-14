# 🔐 Diffie-Hellman Key Exchange

## 📜 Definition
The **Diffie-Hellman Key Exchange (DHKE)** is a cryptographic protocol that allows two parties to generate a shared secret key over an insecure channel. This shared key can be used for secure communication and encryption.

---

## 🧠 How It Works
1. **Choose a Prime Number (q)** - This acts as the modulus.
2. **Select a Primitive Root (a)** - A number that generates all numbers modulo `q`.
3. **Each Party Selects a Private Key (Xa & Xb)** - Secret random numbers.
4. **Compute Public Keys (Ya & Yb)**:
   - `Ya = (a^Xa) % q`
   - `Yb = (a^Xb) % q`
5. **Exchange Public Keys**
6. **Compute the Shared Secret Key (Ka & Kb)**:
   - `Ka = (Yb^Xa) % q`
   - `Kb = (Ya^Xb) % q`

Since `Ka == Kb`, both parties now have a secure, shared key! 🔑

---

## 🚀 Usage
This Python program simulates the **Diffie-Hellman Key Exchange** between two users (Alice & Bob).

### 📌 Example
**Input:**
```
Enter a prime number: 23
Enter a primitive root: 5
Enter the private key of A: 6
Enter the private key of B: 15
```

**Output:**
```
Public key of A: 8.0
Public key of B: 19.0
Shared key for A: 2.0
Shared key for B: 2.0
```

🎉 Now both A & B have the same secret key (`2.0`) for encrypted communication!

---

## 🎯 How to Run
### 🔗 Run in Google Colab:
[Click Here to Run in Colab 🚀](https://colab.research.google.com/drive/173m2jIRlZCZ0dp9Y7q7vDclmhXrvJPcV?usp=sharing)

### 🏃 Run Locally:
1. Install Python (if not already installed)
2. Copy the script into a file (e.g., `diffie_hellman.py`)
3. Open a terminal and run:
   ```bash
   python diffie_hellman.py
   ```
4. Follow the prompts and input values

---

## 🎯 Applications
- **Secure Communication** 🔒 (e.g., WhatsApp, Signal, VPNs)
- **Key Exchange in Cryptographic Protocols** (e.g., TLS, SSH)
- **Blockchain & Cryptocurrency Security**
- **Military & Confidential Data Transmission** 🛡️

---



