#!/bin/bash

while true; do
    clear
    echo "========================================================="
    echo "          ORB CORE WORKSTATION :: MASTER MAIN FRAME      "
    echo "========================================================="
    echo " 1. Execute Hardened Security Ledger      [ledger.sh]"
    echo " 2. Launch Dynamic Perimeter Net Scanner  [net_scanner.py]"
    echo " 3. Access Cognitive Thought Stream       [thought_stream.py]"
    echo " 4. Run System Mirror Backup Suite       [backup.sh]"
    echo " 5. Exit Workstation Environment"
    echo "========================================================="
    echo -n "Select master operational vector [1-5]: "
    read choice

    case $choice in
        1)
            bash ./ledger.sh ;;
        2)
            python ./net_scanner.py ;;
        3)
            python ./thought_stream.py ;;
        4)
            bash ./backup.sh ;;
        5)
            echo -e "\n[*] Disengaging Master Control Deck stream cleanly. Standby."
            exit 0
            ;;
        *)
            echo -e "\n[!] Invalid vector selection signature."
            echo "Press [Enter] to try again..." ; read
            ;;
    esac
done
