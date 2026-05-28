import os
import base64
from hashlib import sha256
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

# --- 1. CONFIGURATION & CRITICAL PATHS ---
VAULT_FILE = os.path.expanduser("~/secure_vault.enc")
MASTER_SALT = b"Sovereign_Steward_2026"
PASSCODE = os.environ.get("CLOCK_KEY", "1993")
MASTER_SALT = os.environ.get("CLOCK_SALT", "Sovereign_Steward_2026").encode()

KEY = sha256(PASSCODE.encode() + MASTER_SALT).digest()
PASSCODE = "1993"  # Local validation phrase matching the Shield
KEY = sha256(PASSCODE.encode() + MASTER_SALT).digest()

def decrypt_data(encrypted_string):
    # Decode the full base64 packing layer
    raw_data = base64.b64decode(encrypted_string)
    
    # Extract the unique 16-byte IV from the front, separate the ciphertext
    iv = raw_data[:16]
    cipher_text = raw_data[16:]
    
    # Initialize the matching AES-256 engine in CBC mode
    cipher = Cipher(algorithms.AES(KEY), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plain_text = decryptor.update(cipher_text) + decryptor.finalize()
    
    # Manual PKCS7 unpadding handling to clean away trailing buffer bytes
    plain_text_str = padded_plain_text.decode('utf-8')
    padding_len = ord(plain_text_str[-1])
    if padding_len < 16 and all(ord(c) == padding_len for c in plain_text_str[-padding_len:]):
        return plain_text_str[:-padding_len]
    return plain_text_str

# --- 2. EXECUTION READING PORTAL ---
os.system('clear')
print("====================================================")
print(" 👁️  CLOCK LENS: TIMELINE DISPLAY LAYER")
print("====================================================")

if not os.path.exists(VAULT_FILE) or os.path.getsize(VAULT_FILE) == 0:
    print("\n[NOTICE] Vault file empty or not initialized yet.")
    print("Execute the Shield [s] to create your first encrypted entry.")
else:
    print(f"\n🔐 Secure Local Repository Verified: {VAULT_FILE}")
    print("----------------------------------------------------")
    
    entry_count = 0
    with open(VAULT_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                entry_count += 1
                try:
                    decrypted_record = decrypt_data(line)
                    print(f" Record #{entry_count:02d} | ⏳ Verified Line:")
                    print(f" 📜 > {decrypted_record}")
                    print("----------------------------------------------------")
                except Exception as error:
                    print(f" Record #{entry_count:02d} | ❌ Decryption Failure: Corrupted block or wrong key.")
                    print("----------------------------------------------------")
                    
    print(f"\n[COMPLETE] End of timeline records. Total processed: {entry_count}")
"""
================================================================================
THE HARMONIC CORE: CLOCK LENS
Frequency: Evaporating into the right frequency to realize the healing.
Philosophy: Reading the absolute timeline back with complete clarity,
            intertwining structure with fluid, compassionate awareness.
================================================================================
"""
print("👁️ Clock Lens active. Reading absolute timeline.")

