import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox
from Crypto.Cipher import AES
import paramiko
from datetime import datetime

KEY = b'0123456789abcdef0123456789abcdef'  # 32 bytes for AES-256
LOG_FILE = "export_log.txt"

# Logging helper
def log_action(action):
    with open(LOG_FILE, "a") as log:
        log.write(f"[{datetime.now()}] {action}\n")

# Padding for AES
def pad(data):
    return data + b" " * (16 - len(data) % 16)

# Encrypt
def encrypt_file():
    file_path = filedialog.askopenfilename(title="Select File to Encrypt")
    if not file_path:
        return

    cipher = AES.new(KEY, AES.MODE_ECB)
    with open(file_path, 'rb') as f:
        data = f.read()

    encrypted_data = cipher.encrypt(pad(data))
    encrypted_file = file_path + ".aes"
    with open(encrypted_file, 'wb') as f:
        f.write(encrypted_data)

    messagebox.showinfo("Success", f"File Encrypted: {encrypted_file}")
    log_action(f"Encrypted file: {encrypted_file}")

# Decrypt
def decrypt_file():
    file_path = filedialog.askopenfilename(title="Select Encrypted File")
    if not file_path or not file_path.endswith(".aes"):
        messagebox.showerror("Error", "Please select a valid .aes file")
        return

    cipher = AES.new(KEY, AES.MODE_ECB)
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data).strip()
    decrypted_file = file_path.replace(".aes", "_decrypted.txt")
    with open(decrypted_file, 'wb') as f:
        f.write(decrypted_data)

    messagebox.showinfo("Success", f"File Decrypted: {decrypted_file}")
    log_action(f"Decrypted file: {decrypted_file}")

# Generate RSA Key + X.509 Certificate
def generate_certificate():
    try:
        subprocess.run("openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run("openssl rsa -in private_key.pem -pubout -out public_key.pem", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        subprocess.run('openssl req -new -x509 -key private_key.pem -out certificate.pem -days 365 -subj "/CN=SecureUser"', shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        messagebox.showinfo("Success", "X.509 Certificate and RSA keys generated!")
        log_action("Generated RSA key pair and certificate")

        # Show certificate info
        result = subprocess.run("openssl x509 -in certificate.pem -text -noout", shell=True, capture_output=True, text=True)
        cert_info = result.stdout
        messagebox.showinfo("Certificate Info", cert_info[:1000])  # Truncate to 1000 chars for readability

    except subprocess.CalledProcessError:
        messagebox.showerror("Error", "OpenSSL failed. Is it installed and added to PATH?")
        log_action("Certificate generation failed - OpenSSL not found or error occurred")

# SFTP File Transfer
def send_file():
    file_path = filedialog.askopenfilename(title="Select File to Send")
    if not file_path:
        return

    host = host_entry.get()
    username = user_entry.get()
    password = pass_entry.get()

    if not (host and username and password):
        messagebox.showerror("Error", "Enter SFTP details first")
        return

    try:
        transport = paramiko.Transport((host, 22))
        transport.connect(username=username, password=password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        # remote_path = f"/home/{username}/{os.path.basename(file_path)}"
        remote_path = os.path.basename(file_path)  
        sftp.put(file_path, remote_path)

        sftp.close()
        transport.close()

        messagebox.showinfo("Success", f"File Sent to: {remote_path}")
        log_action(f"Sent file: {file_path} to {remote_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send file: {e}")
        log_action(f"SFTP transfer failed: {e}")

# Sign File
def sign_file():
    file_path = filedialog.askopenfilename(title="Select File to Sign")
    if not file_path:
        return

    cmd = f"openssl dgst -sha256 -sign private_key.pem -out {file_path}.sig {file_path}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        messagebox.showinfo("Success", f"File Signed: {file_path}.sig")
        log_action(f"Signed file: {file_path}")
    else:
        messagebox.showerror("Error", "Signing failed")
        log_action(f"Signing failed for file: {file_path}")

# Verify Signature
def verify_signature():
    file_path = filedialog.askopenfilename(title="Select File to Verify")
    if not file_path:
        return

    cmd = f"openssl dgst -sha256 -verify public_key.pem -signature {file_path}.sig {file_path}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

    if "Verified OK" in result.stdout:
        messagebox.showinfo("Success", "Signature is VALID!")
        log_action(f"Verified signature: {file_path} ✔")
    else:
        messagebox.showerror("Error", "Signature is INVALID!")
        log_action(f"Signature verification failed: {file_path} ❌")

# GUI
root = tk.Tk()
root.title("Secure Data Handling")
root.geometry("500x700")
root.configure(bg="#2c3e50")

frame = tk.Frame(root, bg="#34495e", padx=20, pady=20)
frame.pack(pady=20, fill="both", expand=True)

def create_button(text, command):
    return tk.Button(frame, text=text, command=command, font=("Arial", 12, "bold"), fg="white", bg="#e74c3c", padx=10, pady=5, relief="raised", bd=3)

tk.Label(frame, text="Secure Data Handling", font=("Arial", 16, "bold"), fg="white", bg="#34495e").pack(pady=10)
create_button("Encrypt File", encrypt_file).pack(pady=5)
create_button("Decrypt File", decrypt_file).pack(pady=5)

tk.Label(frame, text="SFTP Transfer", font=("Arial", 14, "bold"), fg="white", bg="#34495e").pack(pady=10)
tk.Label(frame, text="Host:", fg="white", bg="#34495e").pack()
host_entry = tk.Entry(frame, font=("Arial", 12))
host_entry.pack()
tk.Label(frame, text="Username:", fg="white", bg="#34495e").pack()
user_entry = tk.Entry(frame, font=("Arial", 12))
user_entry.pack()
tk.Label(frame, text="Password:", fg="white", bg="#34495e").pack()
pass_entry = tk.Entry(frame, show="*", font=("Arial", 12))
pass_entry.pack()
create_button("Send File Securely", send_file).pack(pady=10)

tk.Label(frame, text="Digital Signature", font=("Arial", 14, "bold"), fg="white", bg="#34495e").pack(pady=10)
create_button("Generate X.509 Certificate", generate_certificate).pack(pady=5)
create_button("Sign File", sign_file).pack(pady=5)
create_button("Verify Signature", verify_signature).pack(pady=5)

root.mainloop()
