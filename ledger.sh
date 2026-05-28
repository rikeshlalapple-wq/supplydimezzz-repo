#!/bin/bash
# Off-The-Grid Encrypted Ledger Utility

DATA_FILE=".secure_ledger.dat"

clear
echo "=================================================="
echo "      SECURE LEDGER MULTI-TASK PIPELINE          "
echo "=================================================="
echo "1. Write Encrypted Entry to Ledger"
echo "2. Read and Decrypt Full Ledger"
echo "=================================================="
read -p "Select operational vector [1-2]: " MODE

if [ "$MODE" == "1" ]; then
    read -p "Enter account log/transaction text: " ENTRY
    read -sp "Enter Master Encryption Key: " KEY
    echo ""
    
    # Timestamp the entry and encrypt it inline using ChaCha20
    TIMESTAMP=$(date +"%Y-%m-%d %T")
    COMPLETE_STRING="[$TIMESTAMP] $ENTRY"
    
    # Append the encrypted string as a clean, isolated row
    echo "$COMPLETE_STRING" | openssl enc -chacha20 -a -pbkdf2 -pass "pass:$KEY" >> "$DATA_FILE"
    echo "Entry successfully locked into database matrix."

elif [ "$MODE" == "2" ]; then
    if [ ! -f "$DATA_FILE" ]; then
        echo "Error: Database matrix is currently empty."
        exit 1
    fi
    
    read -sp "Enter Master Decryption Key: " KEY
    echo -e "\n\n--- DECRYPTED LEDGER LOGS ---"
    
    # Decrypt the storage file stream line-by-line
    while read -r line; do
        echo "$line" | openssl enc -chacha20 -d -a -pbkdf2 -pass "pass:$KEY" 2>/dev/null
    done < "$DATA_FILE"
    echo "-----------------------------"
else
    echo "Invalid vector signature."
fi

#!/bin/bash
source .env

# Touch database file if it doesn't exist
touch "$DATA_FILE"

clear
echo "========================================================="
echo "          ENCRYPTED SECURITY LEDGER DATABASE            "
echo "========================================================="
echo "1. Write New Timestamped Entry"
echo "2. Decrypt and Read Ledger Logs"
echo "3. Return to Master Control Deck"
echo "========================================================="
echo -n "Select operation [1-3]: "
read op

if [ "$op" -eq 1 ]; then
    echo -e "\nEnter your security or system log entry below:"
    read -r user_entry
    
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    LOG_LINE="[$TIMESTAMP] $user_entry"
    
    echo -n "Enter Master Passphrase to lock transaction: "
    read -s password
    echo
    
    # Temporarily read existing, append new line, and encrypt the bundle
    (echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null; echo "$LOG_LINE") | \
    openssl enc -chacha20 -salt -pbkdf2 -out "$DATA_FILE.tmp" -pass stdin
    
    mv "$DATA_FILE.tmp" "$DATA_FILE"
    echo "Transaction locked and synced to encrypted storage securely."
    echo "Press [Enter] to continue..." ; read

elif [ "$op" -eq 2 ]; then
    echo -n -e "\nEnter Master Passphrase to decrypt database: "
    read -s password
    echo
    
    echo -e "\n=================== DECRYPTED LEDGER LOGS ==================="
    echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null
    echo "============================================================="
    echo "Press [Enter] to clear decrypted memory stream..." ; read
fi

#!/bin/bash
source .env

# Initialize data container silently if missing
touch "$DATA_FILE"

clear
echo "========================================================="
echo "          ENCRYPTED SECURITY LEDGER DATABASE            "
echo "========================================================="
echo "1. Write New Timestamped Log Entry"
echo "2. Decrypt and Read Ledger Stream"
echo "3. Return to Master Control Deck"
echo "========================================================="
echo -n "Select operational vector [1-3]: "
read op

if [ "$op" -eq 1 ]; then
    echo -e "\nEnter your system log text or data entry:"
    read -r user_entry
    
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    LOG_LINE="[$TIMESTAMP] $user_entry"
    
    echo -n "Set Secret Transaction Passphrase: "
    read -s password
    echo
    
    # Extract, append, and re-lock the secure ledger binary file
    (echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null; echo "$LOG_LINE") | \
    openssl enc -chacha20 -salt -pbkdf2 -out "$DATA_FILE.tmp" -pass stdin 2>/dev/null
    
    mv "$DATA_FILE.tmp" "$DATA_FILE"
    echo -e "\n[ SUCCESS ] Entry encrypted and synchronized to ledger storage."
    echo "Press [Enter] to return..." ; read

elif [ "$op" -eq 2 ]; then
    echo -n -e "\nEnter Secret Master Passphrase to decrypt data: "
    read -s password
    echo
    
    echo -e "\n=================== DECRYPTED LEDGER LOGS ==================="
    echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null
    echo "============================================================="
    echo "Press [Enter] to flush decrypted memory stream..." ; read
fi
#!/bin/bash
source .env

# Initialize data container silently if missing
touch "$DATA_FILE"

clear
echo "========================================================="
echo "          ENCRYPTED SECURITY LEDGER DATABASE            "
echo "========================================================="
echo "1. Write New Timestamped Log Entry"
echo "2. Decrypt and Read Ledger Stream"
echo "3. Return to Master Control Deck"
echo "========================================================="
echo -n "Select operational vector [1-3]: "
read op

if [ "$op" -eq 1 ]; then
    echo -e "\nEnter your system log text or data entry:"
    read -r user_entry
    
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    LOG_LINE="[$TIMESTAMP] $user_entry"
    
    echo -n "Set Secret Transaction Passphrase: "
    read -s password
    echo
    
    # Extract, append, and re-lock the secure ledger binary file
    (echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null; echo "$LOG_LINE") | \
    openssl enc -chacha20 -salt -pbkdf2 -out "$DATA_FILE.tmp" -pass stdin 2>/dev/null
    
    mv "$DATA_FILE.tmp" "$DATA_FILE"
    echo -e "\n[ SUCCESS ] Entry encrypted and synchronized to ledger storage."
    echo "Press [Enter] to return..." ; read

elif [ "$op" -eq 2 ]; then
    echo -n -e "\nEnter Secret Master Passphrase to decrypt data: "
    read -s password
    echo
    
    echo -e "\n=================== DECRYPTED LEDGER LOGS ==================="
    echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null
    echo "============================================================="
    echo "Press [Enter] to flush decrypted memory stream..." ; read
fi
#!/bin/bash
source .env

# Initialize data container silently if missing
touch "$DATA_FILE"

clear
echo "========================================================="
echo "          ENCRYPTED SECURITY LEDGER DATABASE            "
echo "========================================================="
echo "1. Write New Timestamped Log Entry"
echo "2. Decrypt and Read Ledger Stream"
echo "3. Return to Master Control Deck"
echo "========================================================="
echo -n "Select operational vector [1-3]: "
read op

if [ "$op" -eq 1 ]; then
    echo -e "\nEnter your system log text or data entry:"
    read -r user_entry
    
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    LOG_LINE="[$TIMESTAMP] $user_entry"
    
    echo -n "Set Secret Transaction Passphrase: "
    read -s password
    echo
    
    # Extract, append, and re-lock the secure ledger binary file
    (echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null; echo "$LOG_LINE") | \
    openssl enc -chacha20 -salt -pbkdf2 -out "$DATA_FILE.tmp" -pass stdin 2>/dev/null
    
    mv "$DATA_FILE.tmp" "$DATA_FILE"
    echo -e "\n[ SUCCESS ] Entry encrypted and synchronized to ledger storage."
    echo "Press [Enter] to return..." ; read

elif [ "$op" -eq 2 ]; then
    echo -n -e "\nEnter Secret Master Passphrase to decrypt data: "
    read -s password
    echo
    
    echo -e "\n=================== DECRYPTED LEDGER LOGS ==================="
    echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null
    echo "============================================================="
    echo "Press [Enter] to flush decrypted memory stream..." ; read
fi
#!/bin/bash
source .env

# Initialize data container silently if missing
touch "$DATA_FILE"

clear
echo "========================================================="
echo "          ENCRYPTED SECURITY LEDGER DATABASE            "
echo "========================================================="
echo "1. Write New Timestamped Log Entry"
echo "2. Decrypt and Read Ledger Stream"
echo "3. Return to Master Control Deck"
echo "========================================================="
echo -n "Select operational vector [1-3]: "
read op

if [ "$op" -eq 1 ]; then
    echo -e "\nEnter your system log text or data entry:"
    read -r user_entry
    
    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
    LOG_LINE="[$TIMESTAMP] $user_entry"
    
    echo -n "Set Secret Transaction Passphrase: "
    read -s password
    echo
    
    # Extract, append, and re-lock the secure ledger binary file
    (echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null; echo "$LOG_LINE") | \
    openssl enc -chacha20 -salt -pbkdf2 -out "$DATA_FILE.tmp" -pass stdin 2>/dev/null
    
    mv "$DATA_FILE.tmp" "$DATA_FILE"
    echo -e "\n[ SUCCESS ] Entry encrypted and synchronized to ledger storage."
    echo "Press [Enter] to return..." ; read

elif [ "$op" -eq 2 ]; then
    echo -n -e "\nEnter Secret Master Passphrase to decrypt data: "
    read -s password
    echo
    
    echo -e "\n=================== DECRYPTED LEDGER LOGS ==================="
    echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$DATA_FILE" 2>/dev/null
    echo "============================================================="
    echo "Press [Enter] to flush decrypted memory stream..." ; read
fi

