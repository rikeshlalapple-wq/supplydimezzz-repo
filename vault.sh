#!/bin/bash
# High-Speed Automated Encryption/Decryption Script

ACTION=$1
FILE=$2

if [ -z "$ACTION" ] || [ -z "$FILE" ]; then
    echo "Usage: ./vault.sh [encrypt|decrypt] [filename]"
    exit 1
fi

if [ "$ACTION" == "encrypt" ]; then
    echo "Locking down $FILE..."
    openssl enc -chacha20 -a -pbkdf2 -in "$FILE" -out "$FILE.enc"
    if [ $? -eq 0 ]; then
        echo "Encryption successful. Shifting out original file securely."
        rm -f "$FILE"
        echo "Target secured as $FILE.enc"
    fi
elif [ "$ACTION" == "decrypt" ]; then
    echo "Unlocking $FILE..."
    # Strip the .enc extension for the output file
    OUTPUT_FILE="${FILE%.enc}"
    openssl enc -chacha20 -d -a -pbkdf2 -in "$FILE" -out "$OUTPUT_FILE"
    if [ $? -eq 0 ]; then
        echo "Decryption successful. Target restored to $OUTPUT_FILE"
    fi
else
    echo "Invalid option. Use 'encrypt' or 'decrypt'."
fi

#!/bin/bash
source .env

# Ensure secure directories exist
mkdir -p "$BACKUP_DIR"

clear
echo "========================================================="
echo "          CHACHA20 CRYPTOGRAPHIC FILE VAULT             "
echo "========================================================="
echo "1. Encrypt and Vault a Media File (Lock)"
echo "2. Decrypt and Restore a Media File (Unlock)"
echo "3. Return to Main Control Deck"
echo "========================================================="
echo -n "Select vector [1-3]: "
read mode

if [ "$mode" -eq 1 ]; then
    echo -e "\nAvailable Media Categories:"
    ls -1 ~/storage/shared/DCIM/
    echo -n -e "\nEnter folder name (e.g., Camera, Snapchat): "
    read folder
    
    echo -n "Enter exact filename to encrypt (e.g., VID_1234.mp4): "
    read filename
    
    SOURCE_PATH="$HOME/storage/shared/DCIM/$folder/$filename"
    TARGET_PATH="$BACKUP_DIR/$filename.enc"
    
    if [ -f "$SOURCE_PATH" ]; then
        echo -n "Set Secret Master Passphrase: "
        read -s password
        echo
        
        # High-speed ChaCha20 encryption stream
        echo "$password" | openssl enc -chacha20 -salt -pbkdf2 -out "$TARGET_PATH" -pass stdin -in "$SOURCE_PATH"
        
        if [ $? -eq 0 ]; then
            # Securely shred/remove the original from the public gallery so it disappears
            rm "$SOURCE_PATH"
            echo "Success: File encrypted and moved safely into your private vault archive."
        else
            echo "Error: Encryption engine failed."
        fi
    else
        echo "Error: Target media file not found."
    fi
    echo "Press [Enter] to continue..." ; read

elif [ "$mode" -eq 2 ]; then
    echo -e "\nCurrently Vaulted Encrypted Files:"
    ls -1 "$BACKUP_DIR" 2>/dev/null
    
    echo -n -e "\nEnter encrypted filename to restore (e.g., VID_1234.mp4.enc): "
    read enc_file
    
    # Strip the .enc extension to get original name back
    orig_file="${enc_file%.enc}"
    
    echo -n "Enter target folder to restore it to (e.g., Camera): "
    read restore_folder
    
    SOURCE_PATH="$BACKUP_DIR/$enc_file"
    TARGET_PATH="$HOME/storage/shared/DCIM/$restore_folder/$orig_file"
    
    if [ -f "$SOURCE_PATH" ]; then
        echo -n "Enter Secret Master Passphrase: "
        read -s password
        echo
        
        # Decrypt it straight back to its original raw media format
        echo "$password" | openssl enc -chacha20 -d -salt -pbkdf2 -in "$SOURCE_PATH" -pass stdin -out "$TARGET_PATH"
        
        if [ $? -eq 0 ]; then
            rm "$SOURCE_PATH"
            echo "Success: Media fully decrypted and restored to your phone's local gallery folder!"
        else
            echo "Error: Decryption failed. Incorrect passphrase."
        fi
    else
        echo "Error: Encrypted file not found."
    fi
    echo "Press [Enter] to continue..." ; read
fi

        if [ $? -eq 0 ]; then
            rm "$SOURCE_PATH"
            echo "Success: Media fully decrypted and restored!"
            
            # Automatically trigger native OS visual playback for the operator
            echo "Launching file visual playback layer..."
            termux-open "$TARGET_PATH"

