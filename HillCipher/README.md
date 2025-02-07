# Hill Cipher Encryption in Python

This is a simple implementation of the **Hill Cipher** encryption algorithm using **NumPy**.

## How It Works

- The program encrypts a given plaintext using **matrix multiplication**.
- It converts characters to numerical values (`A=0, B=1, ..., Z=25`).
- If the plaintext length is not a multiple of the key matrix size, it is padded with `X`.
- The encryption is performed using **modular arithmetic** with matrix multiplication.
- The encrypted text is then converted back to letters.

## Prerequisites

Make sure you have **Python** installed with the following package:

```bash
pip install numpy
```

## Usage

Run the script and enter the plaintext to encrypt.


## Example

```plaintext
Input:  HELLO


Output: ZEBBWX
```

## Notes

- The key matrix should be **invertible modulo 26** for decryption.
- The script currently **only supports encryption**.
- Ensure that the key matrix is **square (n × n)**.


---
Happy Encrypting! 🔐
