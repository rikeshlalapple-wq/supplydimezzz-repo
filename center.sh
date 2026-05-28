#!/bin/bash
# Command Center Dashboard - Master Core

clear
echo "=================================================="
echo "    COMMAND CENTER INITIALIZED // OPERATOR STATUS   "
echo "=================================================="

TOR_CHECK=$(curl --socks5-hostname 127.0.0.1:9050 -s https://check.torproject.org/api/ip | grep -o '"IsTor":true')

if [ "$TOR_CHECK" == '"IsTor":true' ]; then
    echo -e "NETWORK STATUS: [\e[32m SECURE / TOR ACTIVE \e[0m]"
    EXIT_IP=$(curl --socks5-hostname 127.0.0.1:9050 -s https://check.torproject.org/api/ip | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -n 1)
    echo "MASKED TERMINAL IP: $EXIT_IP"
else
    echo -e "NETWORK STATUS: [\e[31m CLEAR NET / EXPOSED \e[0m]"
    echo "WARNING: Tor pipeline unmapped."
fi
echo "=================================================="
echo "1. Run Automated File Vault (ChaCha20)"
echo "2. Access Encrypted Ledger Database"
echo "3. Audit Live Network Circuit"
echo "4. Exit Command Center"
echo "=================================================="
read -p "Select operational protocol [1-4]: " CHOICE

case $CHOICE in
    1)
        read -p "Enter action [encrypt/decrypt]: " ACT
        read -p "Enter target filename: " FNAME
        ./vault.sh "$ACT" "$FNAME"
        ;;
    2)
        ./ledger.sh
        ;;
    3)
        echo "Auditing localized routing matrix..."
        echo "--------------------------------------------------"
        curl -v --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/
        ;;
    4)
        echo "Standing down. Perimeter remains active."
        exit 0
        ;;
    *)
        echo "Invalid protocol signature."
        ;;
esac

#!/bin/bash
# Command Center Dashboard - Master Core

clear
echo "=================================================="
echo "    COMMAND CENTER INITIALIZED // OPERATOR STATUS   "
echo "=================================================="

# Check local Tor routing state
TOR_CHECK=$(curl --socks5-hostname 127.0.0.1:9050 -s https://check.torproject.org/api/ip | grep -o '"IsTor":true')

if [ "$TOR_CHECK" == '"IsTor":true' ]; then
    echo -e "NETWORK STATUS: [\e[32m SECURE / TOR ACTIVE \e[0m]"
    EXIT_IP=$(curl --socks5-hostname 127.0.0.1:9050 -s https://check.torproject.org/api/ip | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -n 1)
    echo "MASKED TERMINAL IP: $EXIT_IP"
else
    echo -e "NETWORK STATUS: [\e[31m CLEAR NET / EXPOSED \e[0m]"
    echo "WARNING: Tor pipeline unmapped."
fi
echo "=================================================="
echo "1. Run Automated File Vault (ChaCha20)"
echo "2. Access Encrypted Ledger Database"
echo "3. Run Automated Secure Data Backup"
echo "4. Audit Live Network Circuit"
echo "5. Exit Command Center"
echo "=================================================="
read -p "Select operational protocol [1-5]: " CHOICE

case $CHOICE in
    1)
        read -p "Enter action [encrypt/decrypt]: " ACT
        read -p "Enter target filename: " FNAME
        ./vault.sh "$ACT" "$FNAME"
        ;;
    2)
        ./ledger.sh
        ;;
    3)
        ./backup.sh
        ;;
    4)
        echo "Auditing localized routing matrix..."
        echo "--------------------------------------------------"
        curl -v --socks5-hostname 127.0.0.1:9050 https://check.torproject.org/
        ;;
    5)
        echo "Standing down. Perimeter remains active."
        exit 0
        ;;
    *)
        echo "Invalid protocol signature."
        ;;
esac


#!/bin/bash
# Command Center Dashboard - Production Matrix Core
set -uo pipefail

# Infinite Interface Loop
while true; do
    # Load parameters fresh on every cycle
    if [ -f "./.env" ]; then
        source ./.env
    else
        echo "CRITICAL: Master environment configuration file (.env) missing." >&2
        exit 1
    fi

    clear
    echo "=================================================="
    echo "    COMMAND CENTER INITIALIZED // OPERATOR STATUS "
    echo "=================================================="

    # Verify active secure proxy matrix
    TOR_CHECK=$(curl --socks5-hostname "$TOR_PROXY" -s https://check.torproject.org/api/ip | grep -o '"IsTor":true' || true)

    if [ "$TOR_CHECK" == '"IsTor":true' ]; then
        echo -e "NETWORK STATUS: [\e[32m SECURE / TOR ACTIVE \e[0m]"
        EXIT_IP=$(curl --socks5-hostname "$TOR_PROXY" -s https://check.torproject.org/api/ip | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -n 1 || echo "UNKNOWN")
        echo "MASKED TERMINAL IP: $EXIT_IP"
    else
        echo -e "NETWORK STATUS: [\e[31m CLEAR NET / EXPOSED \e[0m]"
        echo "WARNING: Proxy pipeline unmapped."
    fi

    echo "=================================================="
    echo "1. Run Automated File Vault (ChaCha20)"
    echo "2. Access Encrypted Ledger Database"
    echo "3. Run Automated Secure Data Backup"
    echo "4. Audit Live Network Circuit"
    echo "5. Run Home Network Perimeter Scan"
    echo "6. Exit Command Center"
    echo "=================================================="
    read -p "Select operational protocol [1-6]: " CHOICE

    case "$CHOICE" in
        1)
            read -p "Enter action [encrypt/decrypt]: " ACT
            read -p "Enter target filename: " FNAME
            if [ -f "./vault.sh" ]; then ./vault.sh "$ACT" "$FNAME"; else echo "Vault engine missing."; fi
            read -p "Press [Enter] to continue..."
            ;;
        2)
            if [ -f "./ledger.sh" ]; then ./ledger.sh; else echo "Ledger script missing."; fi
            ;;
        3)
            if [ -f "./backup.sh" ]; then ./backup.sh; else echo "Backup engine missing."; fi
            read -p "Press [Enter] to continue..."
            ;;
        4)
            echo "Auditing localized routing matrix..."
            echo "--------------------------------------------------"
            curl -v --socks5-hostname "$TOR_PROXY" https://check.torproject.org/ || true
            read -p "Press [Enter] to continue..."
            ;;
        5)
            if [ -f "./recon.sh" ]; then ./recon.sh; else echo "Recon tool missing."; fi
            ;;
        6)
            echo "Standing down. Perimeter remains active."
            exit 0
            ;;
        *)
            echo "Invalid protocol signature."
            sleep 1.5
            ;;
    esac
done

#!/bin/bash
# ==============================================================================
# CORE ARCHITECTURE: INTEGRATED PRODUCTION COMMAND CENTER INTERFACE
# ==============================================================================
set -uo pipefail

# Initialize Persistent Control Loop Workspace
while true; do
    # Source master variables dynamically on each environment cycle
    if [ -f "./.env" ]; then
        source ./.env
    else
        echo "[CRITICAL] Global configuration matrix (.env) cannot be resolved." >&2
        exit 1
    fi

    clear
    echo "======================================================================"
    echo "    COMMAND CENTER INITIALIZED // COMPONENT RUNTIME SECURITY MATRIX   "
    echo "======================================================================"

    # Perform active evaluation of proxy encryption transit tunnel
    TOR_VALIDATION=$(curl --socks5-hostname "$TOR_PROXY" -s https://check.torproject.org/api/ip | grep -o '"IsTor":true' || true)

    if [ "$TOR_VALIDATION" == '"IsTor":true' ]; then
        echo -e "ROUTING LAYER STATUS : [\e[32m MATRIX ACTIVE // SECURE ANONYMOUS PROXY \e[0m]"
        MASKED_IP=$(curl --socks5-hostname "$TOR_PROXY" -s https://check.torproject.org/api/ip | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | head -n 1 || echo "UNKNOWN")
        echo "MASKED TERMINAL WAN  : $MASKED_IP"
    else
        echo -e "ROUTING LAYER STATUS : [\e[31m WARNING // CLEAR-TEXT WAN INTERFACE EXPOSED \e[0m]"
        echo "OPERATIONAL NOTE     : Secure tunneling daemon unmapped."
    fi

    echo "======================================================================"
    echo "1. Execute Encryption Pipeline (ChaCha20 Engine File Vault)"
    echo "2. Interface with Secure Encrypted Ledger Database"
    echo "3. Run Automated System Data Backup & Directory Compression"
    echo "4. Execute Real-Time Network Route Integrity Audit"
    echo "5. Run Passive Subnet Interceptor (Xfinity Home Perimeter Scan)"
    echo "6. Safe Disconnect / Terminate Command Center Environment"
    echo "======================================================================"
    echo ""
    read -p "Select target operational vector [1-6]: " PROTOCOL_CHOICE

    case "$PROTOCOL_CHOICE" in
        1)
            read -p "Enter operation mode [encrypt/decrypt]: " VAULT_MODE
            read -p "Enter literal target path/filename: " TARGET_FILE
            if [ -f "./vault.sh" ]; then 
                ./vault.sh "$VAULT_MODE" "$TARGET_FILE" || echo "[ERROR] Crypto sequence failed."
            else 
                echo "[ERROR] Encryption module unlinked."
            fi
            read -p "Sequence paused. Press [Enter] to resume workspace loop..."
            ;;
        2)
            if [ -f "./ledger.sh" ]; then 
                ./ledger.sh || echo "[ERROR] Data access error."
            else 
                echo "[ERROR] Ledger database module unlinked."
            fi
            ;;
        3)
            if [ -f "./backup.sh" ]; then 
                ./backup.sh || echo "[ERROR] Compression stream interrupted."
            else 
                echo "[ERROR] Archive engine unlinked."
            fi
            read -p "Sequence paused. Press [Enter] to resume workspace loop..."
            ;;
        4)
            echo "Auditing live transport layer routing nodes..."
            echo "----------------------------------------------------------------------"
            curl -v --socks5-hostname "$TOR_PROXY" https://check.torproject.org/ || echo "[NETWORK ERROR] Outbound probe failed."
            read -p "Sequence paused. Press [Enter] to resume workspace loop..."
            ;;
        5)
            if [ -f "./recon.sh" ]; then 
                ./recon.sh || echo "[ERROR] Scanner pipeline halted."
            else 
                echo "[ERROR] Reconnaissance sub-component unlinked."
            fi
            ;;
        6)
            echo "Standing down environment modules cleanly. Home perimeter remains active."
            echo "Workspace cleared."
            exit 0
            ;;
        *)
            echo "[INVALID SIGNATURE] Selected code sequence not recognized."
            sleep 1.2
            ;;
    esac
done
# ==============================================================================

clear
echo "========================================================="
echo "       COMMAND CENTER INITIALIZED // OPERATOR STATUS     "
echo "========================================================="
echo "NETWORK STATUS: [ SECURE / TOR ACTIVE ]"
echo "MASKED TERMINAL IP: $MASKED_IP"
echo "========================================================="
echo "1. Run Automated File Vault (ChaCha20)"
echo "2. Access Encrypted Ledger Database"
echo "3. Run Home Network Perimeter Scan"
echo "4. Track Network Changes (Diff Archive)"
echo "5. Exit Command Center"
echo "========================================================="
echo -n "Select operational protocol [1-5]: "
read choice
case $choice in
    1) ./vault.sh ;;
    2) ./ledger.sh ;;
    3) ./recon.sh ;;
    4) 
        echo "Comparing latest security logs..."
        # Finds the two most recent scan logs and shows the difference
        LATEST=$(ls -t network_audits/*.txt 2>/dev/null | head -n 1)
        PREVIOUS=$(ls -t network_audits/*.txt 2>/dev/null | sed -n '2p')
        if [ -n "$LATEST" ] && [ -n "$PREVIOUS" ]; then
            diff -u "$PREVIOUS" "$LATEST"
        else
            echo "Insufficient log history to run a differential audit."
        fi
        echo "Press [Enter] to return..."
        read ;;
    5) echo "Standing down. Perimeter remains active." ; exit 0 ;;
    *) echo "Invalid option." ; sleep 1 ;;
esac
