# Monoalphabetic-Cipher
A simple and user-friendly implementation of the Monoalphabetic Cipher in Python for encryption and decryption of messages using a fixed substitution alphabet.


- [Introduction](#introduction)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)


## Introduction
The Monoalphabetic Cipher is a type of substitution cipher where each letter in the plaintext is replaced with a corresponding letter from a predefined mapping. This implementation provides an easy-to-use interface for encrypting and decrypting messages.

## Features
✅ Encrypts plaintext messages using a predefined substitution alphabet.  
✅ Decrypts ciphertext messages back to the original plaintext.  
✅ Preserves non-alphabetic characters without modification.  
✅ Simple and easy-to-use Python script.  

## How It Works
The script defines two mappings:
- `p = 'abcdefghijklmnopqrstuvwxyz'` (Plaintext alphabet)
- `ch = 'QWERTYUIOPASDFGHJKLZXCVBNM'` (Ciphertext alphabet)

Each letter from the input is replaced with its corresponding letter from the predefined mapping during encryption, and vice versa during decryption.

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository or download the script:
```sh
$ git clone https://github.com/yourusername/monoalphabetic-cipher.git
$ cd monoalphabetic-cipher
```
2. Run the script:
```sh
$ python monoalphabetic_cipher.py
```

## Usage
1. Enter the message you want to encrypt (input should be in lowercase).
2. Copy the encrypted output.
3. Enter the encrypted message to decrypt (input should be in uppercase).
4. The original message is displayed.

## Example
```sh
$ python monoalphabetic_cipher.py
ENTER THE MESSAGE TO ENCRYPT: resultsareout
Encrypted message: KTLXSZLQKTGXZ
ENTER THE MESSAGE TO DECRYPT: KTLXSZLQKTGXZ
Decrypted message: resultsareout
```

