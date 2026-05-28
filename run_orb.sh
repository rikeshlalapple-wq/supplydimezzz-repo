#!/bin/bash

while true; do
    clear
    echo "========================================================="
    echo "          ORB CORE WORKSTATION :: MASTER MAIN FRAME      "
    echo "========================================================="
    echo " 1. Execute Hardened Security Ledger      [ledger.sh]"
    echo " 2. Launch Dynamic Perimeter Net Scanner  [net_scanner.py]"
    echo " 3. Run System Mirror Backup Suite       [backup.sh]"
    echo " 4. Exit Workstation Environment"
    echo "========================================================="
    echo -n "Select master operational vector [1-4]: "
    read choice

    case $choice in
        1)
            if [ -f "./ledger.sh" ]; then
                bash ./ledger.sh
            else
                echo -e "\n[!] Error: ledger.sh missing from root tree."
                echo "Press [Enter] to return..." ; read
            fi
            ;;
        2)
            if [ -f "./net_scanner.py" ]; then
                echo -e "\n[*] Initializing Network Environment..."
                python ./net_scanner.py
            else
                echo -e "\n[!] Error: net_scanner.py missing from root tree."
                echo "Press [Enter] to return..." ; read
            fi
            ;;
        3)
            if [ -f "./backup.sh" ]; then
                bash ./backup.sh
            else
                echo -e "\n[*] PHASE PREVIEW: Backup automation loop configuration is next."
                echo "Press [Enter] to return..." ; read
            fi
            ;;
        4)
            echo -e "\n[*] Disengaging Master Control Deck stream cleanly. Standby."
            exit 0
            ;;
        *)
            echo -e "\n[!] Invalid vector selection signature."
            echo "Press [Enter] to try again..." ; read
            ;;
    esac
done
