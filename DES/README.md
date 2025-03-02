# 📌 Binary Key Generation for DES

## 📖 Overview
This Python script generates a set of **8 unique cryptographic keys** from a user-inputted string by performing **binary transformations, bitwise shifts, and random bit removals**. The process involves converting the input into binary, manipulating it using bitwise operations, and selectively removing bits to create secure cryptographic keys. This approach is inspired by key-generation mechanisms used in encryption algorithms like **DES (Data Encryption Standard)**.

---

## 🛠️ How It Works
1. **🔢 Binary Conversion:**
   - The input string is converted into an **8-bit binary representation**.
2. **🧩 Binary Processing:**
   - The binary data is split into **left and right halves**, excluding the first bit of each 8-bit segment.
3. **🔄 Bitwise Shifting:**
   - The left and right halves undergo bitwise shifting based on a predefined list:
     ```python
     lt = [2,3,6,7,1,6,5,9]
     ```
4. **🔑 Key Generation:**
   - A new key is formed by **combining the shifted halves**.
   - **8 random bits are removed** to introduce randomness.
5. **📜 Key Output:**
   - The script prints **8 unique cryptographic keys**.

---

## 💻 Usage Instructions
1. **Run the script** in a Python environment (e.g., Google Colab, Jupyter Notebook, or a local Python IDE).
2. **Enter a string** when prompted.
3. The script will process the input and generate **8 unique keys**.

---

## 📌 Example
**Input:**
```
Enter a string: Hello
```
**Binary Conversion:**
```
01001000 01100101 01101100 01101100 01101111
```
**Generated Keys:**
```
Key 1 = 101010011011101
Key 2 = 011110101010001
Key 3 = 110001011010010
...
Key 8 = 110101110010011
```

---

## 🌟 Applications
✅ **Cryptographic Key Generation** – Used for symmetric encryption techniques like **DES & AES**.  
✅ **Randomized Hashing** – Creating **unique hashed representations** of sensitive data.  
✅ **Data Security & Obfuscation** – Protecting passwords, credentials, and confidential information.  
✅ **Steganography & Digital Watermarking** – Embedding secret information within digital content.  

---

## 🔗 Run on Google Colab
[![Run on Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1nsbgfe9ZBfGteE94Kh4tnvlglr9raUZH)

---

