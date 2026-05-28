#!/usr/bin/env python3
import os
import glob
import base64
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

VAULT_DIR = os.path.expanduser("~/workspace/vault")

def derive_ram_key(passphrase: str) -> Fernet:
    salt = b'\x8a\x2f\x9d\xc1\x14\xee\xbc\x77\xaa\x4d\x01\x99\xfb\xcc\x32\x0e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    derived_bytes = kdf.derive(passphrase.encode('utf-8'))
    return Fernet(base64.urlsafe_b64encode(derived_bytes))

print("\n" + "="*60)
print("  [!] STREAM DECK DECRYPTION LOGIC: ENTRY VERIFICATION")
print("="*60)

user_pass = input(" orb-core@decryption-gate:# ").strip()

try:
    cipher_suite = derive_ram_key(user_pass)
except Exception as e:
    print(f"[!] Access initialization failure: {str(e)}")
    sys.exit(1)

enc_files = glob.glob(os.path.join(VAULT_DIR, "ledger_*.enc"))
if not enc_files:
    print("[-] No encrypted files found in vault.")
    sys.exit(0)

print(f"\n=== COGNITIVE DATA DECRYPTION ENGINE: {len(enc_files)} NODES DETECTED ===")

for file_path in sorted(enc_files):
    filename = os.path.basename(file_path)
    print(f"\n[+] Processing Stream Node: {filename}")
    print("-" * 50)
    try:
        with open(file_path, "rb") as f:
            encrypted_data = f.read()
        
        decrypted_text = cipher_suite.decrypt(encrypted_data).decode('utf-8')
        print(decrypted_text)
    except Exception:
        print("[!] ACCESS REFUSED: Invalid Passphrase Signature for this Node Matrix.")
    print("-" * 50)
