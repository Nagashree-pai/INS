# 🔐 Secure Data Handling - Python Mini Project

## 📌 Overview

This mini-project provides a user-friendly Python GUI application for handling sensitive data securely.
- **Secure Data Storage** with AES encryption/decryption  
- **Secure Data Transmission** using SFTP  
- **Digital Signature & X.509 Certificate** generation and verification using RSA and OpenSSL  

It is built with **Tkinter** (GUI), **PyCryptodome** (for AES), **Paramiko** (for SFTP), and **OpenSSL** (for signing and certificates).

---

## 🎯 Features

### 1. 🔒 Secure Data Storage
- AES-256 file encryption using ECB mode
- Secure decryption with proper padding
- Simple interface to select and process files

### 2. 📤 Secure Data Transmission
- Send files securely over SFTP (port 22)
- Connects using host, username, and password
- Uses Paramiko library for SSH/SFTP connection

### 3. 🖊️ Digital Signature & X.509 Certificates
- Generate RSA private/public key pair
- Create X.509 certificate with OpenSSL
- Sign files using SHA-256
- Verify file authenticity using digital signature

---


## 📦 Requirements

- **Python 3.6+**
- **OpenSSL**
  - Make sure OpenSSL is installed and added to your system PATH.
  - ✅ To check:  
    ```bash
    openssl version
    ```

- **Python Libraries**
  ```bash
  pip install pycryptodome paramiko
  ```

---

## ▶️ How to Run

1. Save the script as `secure_gui.py`
2. Run the app using:

```bash
python secure_gui.py
```

---

## 🖥 GUI Overview

- 🔐 **Encrypt File**: Select and encrypt any file (creates `.aes` file)
- 🔓 **Decrypt File**: Choose a `.aes` file to decrypt (restores original)
- 📄 **Generate Certificate**: Creates:
  - `private_key.pem`
  - `public_key.pem`
  - `certificate.pem`
- 🖊️ **Sign File**: Signs a file using `private_key.pem` (creates `.sig`)
- ✅ **Verify Signature**: Verifies using `public_key.pem`
- 🌐 **Send File Securely**: Transfers file to remote server via SFTP

---

## 💡 Usage Examples

### 1. 🔐 Encrypting a File
Click **"Encrypt File"**, select any file (e.g., `example.txt`).  
**Output**: `example.txt.aes`

### 2. 🔓 Decrypting a File
Click **"Decrypt File"**, choose `example.txt.aes`.  
**Output**: `example.txt_decrypted.txt`

### 3. 📜 Generating Certificate
Click **"Generate X.509 Certificate"**  
Generates:
- `private_key.pem`
- `public_key.pem`
- `certificate.pem`

### 4. 🖊️ Signing a File
Click **"Sign File"**, select a file to sign.  
**Output**: `example.txt.sig`

### 5. ✅ Verifying Signature
Click **"Verify Signature"**, select `example.txt`  
Ensure `example.txt.sig` exists in the same location.

### 6. 🌐 SFTP Transfer
Enter:
- **Hostname** (e.g., `192.168.1.10`)
- **Username**
- **Password**

Click **"Send File Securely"**, then select the file to upload.

---

## 📁 Output Files

| File               | Description                |
|--------------------|----------------------------|
| `*.aes`            | Encrypted file             |
| `*_decrypted.txt`  | Decrypted output           |
| `private_key.pem`  | RSA Private Key            |
| `public_key.pem`   | RSA Public Key             |
| `certificate.pem`  | X.509 Certificate          |
| `*.sig`            | Digital Signature          |
| `export_log.txt`   | Operation log              |

---

## ⚠️ Security Notes

- The AES-256 key is **hardcoded** – meant for demo use only.  
  ➤ Replace it with a secure key management system in production.
- **ECB mode** is used – it's not secure for highly sensitive data.  
  ➤ Use CBC or GCM for real-world applications.
- SFTP credentials are entered securely at runtime, but not stored.  
  ➤ Prefer SSH key-based login in production environments.

---

## 🔧 File Structure

```
secure_gui.py           # Main Application
export_log.txt          # Operation log (auto-created)
*.aes                   # Encrypted files
*_decrypted.txt         # Decrypted files
*.sig                   # Signature files
private_key.pem         # RSA Private Key
public_key.pem          # RSA Public Key
certificate.pem         # X.509 Certificate
```

---
## 🛠 Applications

-Secure communication in cloud-based apps

-Confidential file storage and sharing

-Digital signing for authenticity and integrity

-Educational demonstration of cybersecurity principles

-Secure submission system for assignments and reports

---
