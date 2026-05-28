import json
import socket
from concurrent.futures import ThreadPoolExecutor

def check_host(ip, port=80, timeout=0.5):
    """
    Attempts to establish a basic socket connection to a host.
    This works natively on Android without root or interface access.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        # Tries to connect to a common web port or standard gateway ping response
        s.connect((ip, port))
        s.close()
        return {"ip_address": ip, "status": "active", "method": "socket_connect"}
    except (socket.timeout, ConnectionRefusedError):
        # A ConnectionRefusedError means the host is alive but the port is closed
        return {"ip_address": ip, "status": "active", "method": "host_responsive"}
    except Exception:
        return None

def run_network_audit():
    # Target your specific home gateway subnet
    subnet_base = "10.0.0."
    print(f"[*] Initializing high-speed user-space sweep on {subnet_base}0/24...")
    
    discovered_devices = []
    ips_to_scan = [f"{subnet_base}{i}" for i in range(1, 255)]
    
    # Use 50 parallel worker threads to scan the entire subnet in seconds
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(check_host, ips_to_scan)
        
        for result in results:
            if result:
                discovered_devices.append(result)
                
    return discovered_devices

if __name__ == "__main__":
    audit_results = run_network_audit()
    
    print("\n--- Consolidated Network Verdict ---")
    print(json.dumps(audit_results, indent=2))
