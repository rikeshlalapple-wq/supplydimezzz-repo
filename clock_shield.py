"""
================================================================================
THE HARMONIC CORE: CLOCK SHIELD
Frequency: Intentional commands running smoothly, minimizing friction.
Philosophy: Letting the logic flow effortlessly to protect boundaries 
            and operate entirely under sovereign command.
================================================================================
"""

import os
import base64
from hashlib import sha256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# --- CONFIG & LOCAL STORAGE ---
VAULT = os.path.expanduser("~/secure_vault.enc")
PASSCODE = os.environ.get("CLOCK_KEY", "1993")
MASTER_SALT = os.environ.get("CLOCK_SALT", "Sovereign_Steward_2026").encode()

KEY = sha256(PASSCODE.encode() + MASTER_SALT).digest()
PASSCODE = os.environ.get("CLOCK_KEY", "1993")
MASTER_SALT = os.environ.get("CLOCK_SALT", "Sovereign_Steward_2026").encode()

KEY = sha256(PASSCODE.encode() + MASTER_SALT).digest()


def encrypt(text):
    iv = os.urandom(16)
    pad_len = 16 - (len(text) % 16)
    padded = text + (chr(pad_len) * pad_len)
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv), backend=default_backend())
    engine = cipher.encryptor()
    ciphertext = engine.update(padded.encode()) + engine.finalize()
    return base64.b64encode(iv + ciphertext).decode('utf-8')

# --- PORTAL INTERFACE ---
os.system('clear')
print("====================================================")
print(" 🛡️  CLOCK SHIELD: SECURE ENTRY VAULT")
print("====================================================")

entry = input("\nEnter your secure timeline record:\n✍️  > ")

if entry.strip():
    try:
        secret_string = encrypt(entry)
        with open(VAULT, "a") as f:
            f.write(secret_string + "\n")
        print("\n[SUCCESS] Entry encrypted via AES-256 and locked.")
    except Exception as e:
        print(f"\n[ERROR] Encryption failed: {e}")
else:
    print("\n[CANCELLED] Empty line.")
