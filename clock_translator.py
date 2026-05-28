import os
import socket

def scan_baseline(host):
    print(f"\n📡 [LAYER 1] Running Baseline Scan on: {host}...")
    common_ports = [22, 23, 80, 443, 554, 8080, 9100]
    open_ports = []
    
    for port in common_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1.0)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"🟢 [OPEN] Channel {port}")
                open_ports.append(port)
            sock.close()
        except socket.gaierror:
            print(f"⚠️  [ERROR] Invalid address coordinate: {host}")
            return None
    return open_ports

def scan_heuristics(host):
    print(f"\n🕵️‍♂️ [LAYER 2] Analyzing Heuristic Signatures on: {host}...")
    stealth_ports = [8081, 8443, 9000, 9999]
    detected = []
    
    for port in stealth_ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.5)
            result = sock.connect_ex((host, port))
            if result == 0:
                print(f"⚠️  [ALERT] Non-standard open channel detected: {port}")
                detected.append(port)
            sock.close()
        except Exception:
            pass
    return detected

def main_control_loop():
    while True:
        os.system('clear')
        print("==================================================")
        print("🌀 MATRIX COMMAND: MULTI-LAYER SCANNER")
        print("==================================================")
        print("1. Run Baseline Layer Scan")
        print("2. Run Heuristic Pattern Scan")
        print("3. Execute Full Multi-Layer Sweep")
        print("4. Terminate Workstation Session")
        print("==================================================")
        
        choice = input("\nEnter operation level (1-4): ").strip()
        
        if choice == '4':
            print("\n🔒 Session cleanly closed. Standing down.")
            break
            
        if choice in ['1', '2', '3']:
            target = input("Enter target IP address (Default: 127.0.0.1): ").strip()
            if not target:
                target = "127.0.0.1"
                
            if choice == '1' or choice == '3':
                scan_baseline(target)
            if choice == '2' or choice == '3':
                scan_heuristics(target)
                
            input("\nSequence finished. Press Enter to loop back...")
        else:
            input("\n⚠️ Invalid selection. Press Enter to refresh...")

if __name__ == "__main__":
    main_control_loop()
