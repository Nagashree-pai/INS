# Playfair-Cipher
A Python implementation of the Playfair Cipher for encrypting and decrypting text using a key-based 5x5 matrix.

- [Introduction](#introduction)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)


## Introduction
The Playfair Cipher is a digraph substitution cipher that encrypts pairs of letters in plaintext using a 5x5 key matrix. It replaces repeating letters and adjusts odd-length messages by adding filler characters.

## Features
✅ Encrypts text using a Playfair matrix.  
✅ Decrypts ciphertext back to its original plaintext.  
✅ Handles odd-length plaintext by appending an 'X'.  
✅ Ignores spaces and treats 'J' as 'I'.  
✅ Simple Python implementation with easy-to-follow logic.  

## How It Works
1. **Matrix Creation**: A 5x5 matrix is generated using the key.
2. **Position Finding**: Each letter's position is determined in the matrix.
3. **Encryption**: Letters in the same row/column shift accordingly; otherwise, a rectangle swap is performed.
4. **Decryption**: Reverse of encryption logic.

## Installation
### Prerequisites
- Python 3.x installed on your system.

### Steps
1. Clone this repository or download the script:
```sh
$ git clone https://github.com/yourusername/playfair-cipher.git
$ cd playfair-cipher
```
2. Run the script:
```sh
$ python playfair_cipher.py
```

## Usage
1. Enter the plaintext message.
2. Provide a key to generate the cipher matrix.
3. Copy the encrypted message.
4. Enter the encrypted text to decrypt it back to the original.

## Example
```sh
$ python playfair_cipher.py
Enter the plain text: instruments
Enter the key: monarchy
Encrypted message: GATLMZCLRQXA
Enter the cipher text: gatlmzclrqxa
Enter the key: monarchy
Decrypted message: INSTRUMENTSX
```
