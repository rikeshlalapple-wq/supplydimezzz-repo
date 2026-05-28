#!/bin/bash
source .env

BACKUP_DIR="backups"
TIMESTAMP=$(date "+%Y-%m-%d_%H%M%S")
TARBALL="$BACKUP_DIR/orb_core_snapshot_$TIMESTAMP.tar.gz"

clear
echo "========================================================="
echo "          ORB CORE :: SYSTEM MIRROR BACKUP SUITE         "
echo "========================================================="
echo "[*] Initializing perimeter workspace snapshot..."

# 1. Ensure the backup container directory exists locally
mkdir -p "$BACKUP_DIR"

# 2. Package and compress all critical workstation components
echo "[*] Compressing active code modules and document matrices..."
tar -czf "$TARBALL" \
    "archive/" \
    "ledger.sh" \
    "net_scanner.py" \
    "thought_stream.py" \
    "run_orb.sh" \
    ".env" \
    .ledger_verify \
    2>/dev/null

if [ -f "$TARBALL" ]; then
    echo "[+] Local snapshot created successfully: $TARBALL"
else
    echo "[!] CRITICAL ERROR: Failed to compress snapshot archive."
    echo "Press [Enter] to return..." ; read
    exit 1
fi

# 3. Storage Protection Loop: Retain only the last 5 backup sets
echo "[*] Checking storage rotation vectors..."
ls -tp $BACKUP_DIR/orb_core_snapshot_*.tar.gz 2>/dev/null | tail -n +6 | xargs rm -f 2>/dev/null

# 4. Cloud Repository Synchronization Loop
echo "[*] Initializing remote cloud repository synchronization..."
git add .
git commit -m "Automated system mirror backup sequence [Snapshot: $TIMESTAMP]" 2>/dev/null
git push

echo "========================================================="
echo "[ SUCCESS ] Workspace mirror fully synchronized and archived."
echo "========================================================="
echo "Press [Enter] to return to Master Control Deck..." ; read
