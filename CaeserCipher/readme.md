Caesar Cipher - Simple Encryption & Decryption

This project demonstrates the **Caesar Cipher**, a basic encryption technique where each letter in the text is shifted by a fixed number of positions in the alphabet.

 🔹 Features
✅ Encrypts plaintext using a shift key  
✅ Decrypts ciphertext back to original text  
✅ Works with both uppercase and lowercase letters  
✅ Keeps special characters unchanged  

---

 📌 How It Works
- Each letter in the text is shifted forward (encryption) or backward (decryption) based on the key.
- The shift wraps around within the 26 English letters (A-Z, a-z).
- Non-alphabet characters remain unchanged.

---

 📂 Files Included
📜 `CaesarCipher.ipynb` - Jupyter Notebook with the complete implementation  
📜 `encrypt()` - Function to encrypt text  
📜 `decrypt()` - Function to decrypt text  

---

 🚀 Quick Start
 Prerequisites
- Python 3.x  
- Jupyter Notebook (or Google Colab)  

 Run the Code
 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/Caesar-Cipher.git
cd Caesar-Cipher
```

#### 2️⃣ Open Jupyter Notebook & Run  
#### 3️⃣ Input Text & Key
```sh
Enter the text to encrypt: hello
Enter the key: 3
Cipher text: khoor
```

#### 4️⃣ Decrypt the Text
```sh
Enter the cipher text: khoor
Enter the key: 3
Plain text: hello
```

---

## 🎯 Examples
### 🔹 Encryption
| Plaintext  | Key | Ciphertext |
|------------|-----|------------|
| `hello`    | 3   | `khoor`    |
| `python`   | 5   | `udymts`   |

### 🔹 Decryption
| Ciphertext | Key | Plaintext  |
|------------|-----|------------|
| `khoor`    | 3   | `hello`    |
| `udymts`   | 5   | `python`   |

---
