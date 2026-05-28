#!/bin/bash
source .env

# Initialize data containers silently if missing
touch "$DATA_FILE"
touch .ledger_verify 2>/dev/null

clear
echo "========================================================="
echo "          ORB CORE HARDENED SECURITY LEDGER             "
echo "========================================================="
echo "1. Write New Verified Transaction Entry"
echo "2. Decrypt and Read Secure Ledger Stream"
echo "3. Return to Master Control Deck"
echo "========================================================="
echo -n "Select operational vector [1-3]: "
read op

# =========================================================
# OPERATIONAL VECTOR 1: WRITE & APPEND WITH VERIFICATION
# =========================================================
if [ "$op" -eq 1 ]; then
    echo -e "\nEnter your system log text or data entry:"
    read -r user_entry

    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    LOG_LINE="[$TIMESTAMP] $user_entry"

    echo -n "Set Secret Transaction Passphrase: "
    read -s password
    echo

    # Integrity Check: Verify key if database already has a history
    if [ -s .ledger_verify ] && [ -s "$DATA_FILE" ]; then
        VERIFY_CHECK=$(openssl enc -chacha20 -d -salt -pbkdf2 -in .ledger_verify -pass pass:"$password" 2>/dev/null)
        if [ "$VERIFY_CHECK" != "VERIFIED" ]; then
            echo -e "\n[!] CRITICAL ERROR: Access Denied. Master Key Mismatch."
            echo "Transaction aborted to protect storage matrix integrity."
            echo "Press [Enter] to exit..." ; read
            exit 1
        fi
    fi

    # Create dynamic backup fail-safe snapshot
    if [ -s "$DATA_FILE" ]; then
        cp "$DATA_FILE" "$DATA_FILE.bak"
        EXISTING_DATA=$(openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" -pass pass:"$password" 2>/dev/null)
    else
        EXISTING_DATA=""
    fi

    # Append new log line and re-lock the vault cleanly
    echo -e "${EXISTING_DATA}\n${LOG_LINE}" | sed '/^$/d' | openssl enc -chacha20 -salt -pbkdf2 -out "$DATA_FILE" -pass pass:"$password"
    
    # Update/Generate hidden key verification block
    echo "VERIFIED" | openssl enc -chacha20 -salt -pbkdf2 -out .ledger_verify -pass pass:"$password"

    # Wipe memory snapshot trace
    rm -f "$DATA_FILE.bak"

    echo -e "\n[ SUCCESS ] Entry encrypted and synchronized to ledger storage."
    echo "Press [Enter] to return..." ; read

# =========================================================
# OPERATIONAL VECTOR 2: DECRYPT & SECURE VIEWPORT
# =========================================================
elif [ "$op" -eq 2 ]; then
    if [ ! -s "$DATA_FILE" ]; then
        echo -e "\n[!] Error: Storage vault matrix is currently empty."
        echo "Press [Enter] to return..." ; read
        exit 1
    fi

    echo -n -e "\nEnter Secret Master Passphrase to decrypt data: "
    read -s password
    echo

    # Verify key integrity before revealing records
    VERIFY_CHECK=$(openssl enc -chacha20 -d -salt -pbkdf2 -in .ledger_verify -pass pass:"$password" 2>/dev/null)
    if [ "$VERIFY_CHECK" != "VERIFIED" ]; then
        echo -e "\n[!] CRITICAL ERROR: Access Denied. Master Key Mismatch."
        echo "Press [Enter] to return..." ; read
        exit 1
    fi

    echo -e "\n=================== DECRYPTED LEDGER LOGS ==================="
    openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" -pass pass:"$password" 2>/dev/null
    echo "============================================================="
    
    echo "Press [Enter] to flush decrypted memory stream from viewport..." ; read
    
    # Security Hygiene: Hard wipe terminal so no plaintext log remains in history
    clear

# =========================================================
# OPERATIONAL VECTOR 3: EXIT CONTROL DECK
# =========================================================
elif [ "$op" -eq 3 ]; then
    echo -e "\n[*] Returning to Master Control Deck..."
    exit 0
else
    echo -e "\n[!] Invalid vector signature."
    echo "Press [Enter] to try again..." ; read
fi
