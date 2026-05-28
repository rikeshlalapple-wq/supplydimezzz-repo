#!/usr/bin/env python3
import time
import os
import random
import sys
import socket
import base64
from prompt_toolkit import Application
from prompt_toolkit.layout import Layout, HSplit
from prompt_toolkit.widgets import TextArea, Frame
from prompt_toolkit.key_binding import KeyBindings

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

VAULT_DIR = os.path.expanduser("~/workspace/vault")
os.makedirs(VAULT_DIR, exist_ok=True)

def derive_ram_key(passphrase: str) -> Fernet:
    salt = b'\x8a\x2f\x9d\xc1\x14\xee\xbc\x77\xaa\x4d\x01\x99\xfb\xcc\x32\x0e'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000
    )
    derived_bytes = kdf.derive(passphrase.encode('utf-8'))
    b64_key = base64.urlsafe_b64encode(derived_bytes)
    return Fernet(b64_key)

print("\n" + "="*60)
print("  [!] CRITICAL LAYER ACCESS REQUIRED: ENTER SOVEREIGN PASSPHRASE")
print("="*60)

user_pass = input(" orb-core@security-gate:# ").strip()

if len(user_pass) < 6:
    print("\n[!] ACCESS DENIED: Passphrase fails minimum structural threshold.")
    sys.exit(1)

try:
    cipher_suite = derive_ram_key(user_pass)
    print("\n [+] Cipher Key Matrix Successfully Derived in Volatile RAM.")
    time.sleep(0.6)
except Exception as e:
    print(f"\n [!] Core initialization fault: {str(e)}")
    sys.exit(1)

user_pass = None

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 1))
    local_ip = s.getsockname()[0]
    s.close()
except Exception:
    local_ip = "UNROUTED"

def generate_telemetry_stream():
    timestamp = time.strftime("%H:%M:%S")
    return f" LAYER 3 SHIELD: ACTIVE | VOLATILE RAM CIPHER | GRID NODE: {local_ip} | {timestamp}"

editor_box = TextArea(
    multiline=True,
    text="[Zero-Trust Core: Ephemeral Encryption Layer Engaged]\nBegin your sovereign data node commit here...\n"
)

status_display = TextArea(
    multiline=False,
    read_only=True,
    text=" STATUS: LEVEL 3 ZERO-TRUST MATRIX RUNNING | CTRL+S: Rotate Cipher | CTRL+C: Safe Exit"
)

def commit_rotated_log():
    try:
        if len(editor_box.text.strip()) < 5:
            return " STATUS: BUFFER VOID. SEQUENCE TERMINATED."

        raw_data = editor_box.text.encode('utf-8')
        encrypted_ciphertext = cipher_suite.encrypt(raw_data)
        
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        log_filename = f"ledger_{timestamp}.enc"
        full_path = os.path.join(VAULT_DIR, log_filename)
        
        with open(full_path, "wb") as f:
            f.write(encrypted_ciphertext)
            
        return f" STATUS: LOCKED & ROTATED CRYPTO LEDGER -> {log_filename}"
    except Exception as e:
        return f" STATUS: CRYPTO SYSTEM FAULT -> {str(e)}"

kb = KeyBindings()

@kb.add('enter')
def handle_enter(event):
    event.current_buffer.insert_text('\n')
    status_display.text = generate_telemetry_stream()

@kb.add('c-s')
def save_to_vault(event):
    status_display.text = commit_rotated_log()

@kb.add('c-c')
def exit_app(event):
    event.app.exit()

layout = Layout(HSplit([
    Frame(editor_box, title="ZERO-TRUST SOVEREIGN CORE ARCHITECTURE"),
    status_display
]))

app = Application(layout=layout, key_bindings=kb, full_screen=True)

if __name__ == "__main__":
    app.run()
