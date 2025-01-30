import tkinter as tk
import re
import hashlib
from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Function to check password strength
def check_password_strength():
    password = entry.get()
    
    # Define strength criteria
    length_error = len(password) < 8
    digit_error = not re.search(r"\d", password)
    uppercase_error = not re.search(r"[A-Z]", password)
    lowercase_error = not re.search(r"[a-z]", password)
    special_char_error = not re.search(r"[@#$%^&*]", password)

    # Determine strength level
    if length_error or digit_error or uppercase_error or lowercase_error or special_char_error:
        strength_label.config(text="Weak Password ❌", fg="red")
    elif len(password) >= 12:
        strength_label.config(text="Strong Password ✅", fg="green")
    else:
        strength_label.config(text="Moderate Password ⚠", fg="orange")

# Function to hash the password (for security)
def hash_password():
    password = entry.get().encode()
    hashed = hashlib.sha256(password).hexdigest()
    hash_label.config(text=f"SHA-256 Hash:\n{hashed}")

# Function to encrypt the password
def encrypt_password():
    password = entry.get().encode()
    encrypted = cipher.encrypt(password)
    encrypt_label.config(text=f"Encrypted Password:\n{encrypted.decode()}")

# Function to reset all fields
def reset_fields():
    entry.delete(0, tk.END)
    strength_label.config(text="")
    hash_label.config(text="")
    encrypt_label.config(text="")

# Function to exit the application
def exit_app():
    root.quit()

# GUI Setup
root = tk.Tk()
root.title("Password Strength Analyzer")
root.geometry("400x400")

# UI Elements
tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=check_password_strength, bg="blue", fg="white").pack(pady=5)
strength_label = tk.Label(root, text="", font=("Arial", 12))
strength_label.pack(pady=5)

tk.Button(root, text="Hash Password", command=hash_password, bg="gray", fg="white").pack(pady=5)
hash_label = tk.Label(root, text="", wraplength=350, font=("Arial", 10))
hash_label.pack(pady=5)

tk.Button(root, text="Encrypt Password", command=encrypt_password, bg="purple", fg="white").pack(pady=5)
encrypt_label = tk.Label(root, text="", wraplength=350, font=("Arial", 10))
encrypt_label.pack(pady=5)

tk.Button(root, text="Reset", command=reset_fields, bg="orange", fg="white").pack(pady=5)
tk.Button(root, text="Exit", command=exit_app, bg="red", fg="white").pack(pady=5)

root.mainloop()
