#!/usr/bin/env python3
import os
import sys
import time

def clear_screen():
    os.system('clear')

def show_header():
    print("=====================================================================")
    print("    O R B   C O R E   W O R K S T A T I O N   ::   M A I N   C O N S O L E   ")
    print("=====================================================================")
    print("[ COHERENCE: OPTIMAL ]  [ SIGNAL: 40 Hz ]  [ ENVIRONMENT: TERMUX ]")
    print("---------------------------------------------------------------------")

def wait_for_keypress(message):
    """Waits for a single keypress and completely flushes input buffers to prevent ghosting."""
    print(message, end="", flush=True)
    try:
        # Standard Unix low-level terminal reader
        import tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    except ImportError:
        # Fallback if termios is entirely locked out
        sys.stdin.readline()
    print()

def main_menu():
    while True:
        clear_screen()
        show_header()
        print("  1. Network Diagnostic Tool      (Live Subnet Host Map Scan)")
        print("  2. System Ledger Management     (Secure Processing / Data Sovereign Logs)")
        print("  3. Recalibrate Pipeline         (Run 40 Hz Gamma Alignment Simulator)")
        print("  4. Drop Connection              (Exit Terminal Workspace)")
        print("  5. View Decrypted Vault Ledger  (Read-Only Cryptographic Stream Deck)")
        print("---------------------------------------------------------------------")
        
        try:
            choice = input("orb-core@operator:~# ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n[-] Signal Interrupted. Resetting console channel...")
            time.sleep(1)
            continue

        if choice == "1":
            os.system('python3 ~/net_scanner.py')
            wait_for_keypress("\n[Radar Scan Complete] Tap ANY KEY to snap back to Main Console...")
        elif choice == "2":
            print("\n[*] Transitioning to Secure Cryptographic Writing Canvas...")
            time.sleep(0.5)
            os.system('python3 ~/workspace_core.py')
        elif choice == "3":
            os.system('python3 ~/recalibrate_40hz.py')
            wait_for_keypress("\n[Recalibration Complete] Tap ANY KEY to snap back to Main Console...")
        elif choice == "4":
            print("\n[-] Dropping Connection. Exiting Workspace safely.")
            break
        elif choice == "5":
            print("\n[*] Booting Cognitive Data Decryption Engine...")
            print("---------------------------------------------------------------------")
            os.system('python3 ~/vault_reader.py')
            print("---------------------------------------------------------------------")
            wait_for_keypress("\n[Matrix Scan Complete] Tap ANY KEY to snap back to Main Console...")
        else:
            if choice != "":
                print(f"\n[!] Node Input Command '{choice}' unknown to routing system.")
                time.sleep(1.2)

if __name__ == "__main__":
    main_menu()
