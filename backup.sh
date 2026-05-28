#!/bin/bash
# Localized Secure Backup Archive Pipeline

BACKUP_DIR="./secure_archives"
DATA_FILE=".secure_ledger.dat"

clear
echo "=================================================="
echo "     SECURE DATA ARCHIVE AUTOMATION PIPELINE      "
echo "=================================================="

# Create the archive repository directory if it doesn't exist yet
if [ ! -d "$BACKUP_DIR" ]; then
    mkdir -p "$BACKUP_DIR"
    echo "Initializing dedicated secure archive directory..."
fi

# Verify the database ledger actually has data before running backup
if [ ! -f "$DATA_FILE" ]; then
    echo "CRITICAL ERROR: No ledger database found to archive."
    exit 1
fi

echo "Scanning operational volumes..."
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_NAME="ledger_snapshot_$TIMESTAMP.tar.gz"

echo "Compressing and locking target matrix rows..."
# Tar and gzip the hidden data file cleanly into the archive folder
tar -czf "$BACKUP_DIR/$BACKUP_NAME" "$DATA_FILE" 2>/dev/null

if [ $? -eq 0 ]; then
    echo "--------------------------------------------------"
    echo -e "SUCCESS: Archive snapshot deployed flawlessly."
    echo "FILE: $BACKUP_DIR/$BACKUP_NAME"
    echo "--------------------------------------------------"
else
    echo "CRITICAL ERROR: Backup pipe failed during compression."
fi

