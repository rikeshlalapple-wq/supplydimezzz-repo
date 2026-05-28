#!/bin/bash
# Professional Subnet Reconnaissance Wrapper
set -euo pipefail

# Ingest master system definitions
if [ -f "./.env" ]; then
    source ./.env
else
    echo "CRITICAL: Global .env blueprint is missing." >&2
    exit 1
fi

clear
echo "=================================================="
echo "       HOME NETWORK SECURITY MONITOR INITIATED     "
echo "=================================================="
echo "Analyzing perimeter vector..."

# Ensure target directories exist safely
mkdir -p "$SCAN_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT_FILE="$SCAN_DIR/home_scan_$TIMESTAMP.txt"

echo "Your Device Terminal IP : $LOCAL_IP"
echo "Targeting Xfinity Subnet: $SUBNET"
echo "--------------------------------------------------"
echo "Scanning active volumes... (Please wait)"

# Execute optimized scan
if nmap -sn "$SUBNET" > "$OUTPUT_FILE"; then
    echo "=================================================="
    echo "SUCCESS: Network footprint mapped cleanly."
    echo "Active Devices Detected On-Screen:"
    echo "--------------------------------------------------"
    grep "Nmap scan report for" "$OUTPUT_FILE" | sed 's/Nmap scan report for //' || echo "No external hosts found."
    echo "=================================================="
    echo "Log persistent snapshot written to: $OUTPUT_FILE"
else
    echo "CRITICAL ERROR: Perimeter scan pipeline interrupted." >&2
    exit 1
fi

read -p "Press [Enter] to cycle back to Command Center..."
#!/bin/bash
# ==============================================================================
# SUB-COMPONENT MODULE: PASSIVE NETWORK SECURITY SCANNER
# ==============================================================================
set -euo pipefail

# Verify and ingest central configuration properties
if [ -f "./.env" ]; then
    source ./.env
else
    echo "[CRITICAL] Infrastructure environment blueprint (.env) is missing." >&2
    exit 1
fi

clear
echo "======================================================================"
echo "          HOME PERIMETER SECURITY MONITORING INTERFACE                "
echo "======================================================================"
echo "Initializing passive packet verification across target gateway..."

# Ensure persistent audit directory tree exists safely
mkdir -p "$SCAN_DIR"

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
SNAPSHOT_LOG="$SCAN_DIR/perimeter_snapshot_$TIMESTAMP.log"

echo "Local Interface Target IP : $LOCAL_IP"
echo "Xfinity Gateway Subnet Vector: $SUBNET"
echo "----------------------------------------------------------------------"
echo "[RUNNING] Compiling active asset fingerprint logs... Please wait."

# Execute non-disruptive ping scanning topology mapping
if nmap -sn "$SUBNET" > "$SNAPSHOT_LOG"; then
    echo "======================================================================"
    echo "[SUCCESS] Subnet perimeter successfully cataloged."
    echo "Currently Active Network Hardware Registrations:"
    echo "----------------------------------------------------------------------"
    
    # Filter and display raw node signatures cleanly for rapid verification
    grep "Nmap scan report for" "$SNAPSHOT_LOG" | sed 's/Nmap scan report for //' || echo "No external clients responded."
    
    echo "======================================================================"
    echo "Persistent diagnostic log written to: $SNAPSHOT_LOG"
else
    echo "[CRITICAL ERROR] Subnet scan pipeline aborted unexpectedly." >&2
    exit 1
fi

echo "----------------------------------------------------------------------"
read -p "Press [Enter] to cycle execution back to the Master Control Deck..."

