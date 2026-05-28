import nmap

def run_perimeter_audit():
    nm = nmap.PortScanner()
    
    # Dynamic user prompt input
    print("==============================================")
    print("      ORB CORE WORKSTATION :: NETWORK SCAN    ")
    print("==============================================")
    target = input("[?] Enter Target IP Address (e.g., 10.0.0.1): ").strip()
    
    if not target:
        print("[!] Error: No target IP provided. Exiting.")
        return

    print(f"\n[*] Initializing Audit on Vector: {target}")
    print("[*] Probing software signatures (Please wait)...")
    
    # Executing our successful non-root banner-grabbing flags
    nm.scan(target, arguments="-sV --version-intensity 5")
    
    if not nm.all_hosts():
        print(f"\n[!] Audit complete: Host {target} did not respond or has all ports sealed.")
        return
        
    for host in nm.all_hosts():
        print(f"\n[+] Host Detected: {host} ({nm[host].hostname()})")
        print(f"[+] State: {nm[host].state()}")
        for proto in nm[host].all_protocols():
            print(f"    Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                name = nm[host][proto][port]['name']
                version = nm[host][proto][port]['version']
                print(f"    Port: {port}\tState: {state}\tService: {name}\tVersion: {version}")
    print("\n==============================================")

if __name__ == "__main__":
    run_perimeter_audit()
