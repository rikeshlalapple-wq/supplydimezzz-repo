import os
import json
import socket
import subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

# Configuration
LOG_FILE = "network_history.json"
# Defines the first three octets of your 10.0.0.1/24 subnet
SUBNET_PREFIX = "10.0.0." 

def ping_device(ip):
    """Pings an IP address. Returns the IP and hostname if active."""
    # -c 1: send 1 packet. -W 1: wait 1 second for a response
    # redirect output to devnull to keep the terminal clean
    with open(os.devnull, 'w') as devnull:
        try:
            # For Android/Linux, the ping flags are -c and -W
            result = subprocess.run(
                ["ping", "-c", "1", "-W", "1", ip],
                stdout=devnull,
                stderr=devnull
            )
            
            if result.returncode == 0:
                # If active, try to get the hostname (device name)
                try:
                    hostname = socket.gethostbyaddr(ip)[0]
                except socket.herror:
                    hostname = "Unknown Device"
                return {"ip": ip, "name": hostname}
        except Exception:
            pass
    return None

def scan_network_without_root():
    """Scans IPs from .1 to .254 concurrently using threads."""
    active_devices = []
    # Generate all host IPs in the /24 subnet range
    ip_list = [f"{SUBNET_PREFIX}{i}" for i in range(1, 255)]
    
    # ThreadPoolExecutor runs multiple pings at the same time so it doesn't take 4 minutes
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(ping_device, ip_list)
        for res in results:
            if res:
                active_devices.append(res)
                
    return active_devices

def load_history():
    if not os.path.exists(LOG_FILE):
        return {}
    try:
        with open(LOG_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_history(history_data):
    with open(LOG_FILE, 'w') as f:
        json.dump(history_data, f, indent=4)

def process_and_log_results(current_devices):
    history = load_history()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\nScan complete at {timestamp}")
    print(f"Found {len(current_devices)} active device(s).")
    print("-" * 55)
    print(f"{'IP Address':<15} | {'Device Hostname':<20} | Status")
    print("-" * 55)

    for device in current_devices:
        ip = device['ip']
        name = device['name']
        
        # Track by IP here since we can't reliably pull MAC addresses without root
        if ip in history:
            status = "Known"
            history[ip]['last_seen'] = timestamp
            history[ip]['hostname'] = name
        else:
            status = "[NEW DEVICE]"
            history[ip] = {
                'first_seen': timestamp,
                'last_seen': timestamp,
                'hostname': name
            }
            
        print(f"{ip:<15} | {name:<20} | {status}")

    save_history(history)
    print("-" * 55)
    print(f"[+] Network log updated in '{LOG_FILE}'.")

if __name__ == "__main__":
    print(f"[*] Initializing non-root scan for range '{SUBNET_PREFIX}1-254'...")
    active_devices = scan_network_without_root()
    process_and_log_results(active_devices)

import socket
import json
import os
from datetime import datetime

def get_local_ip():
    """Triggers internal interface mapping to safely find the sandbox IP"""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # Does not actually connect externally; forces local routing lookup
        s.connect(('8.8.8.8', 1))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

def run_dynamic_scan():
    local_ip = get_local_ip()
    if local_ip == '127.0.0.1':
        print("[!] Unable to resolve local interface. Aborting network scan.")
        return
    
    # Breaks down '10.0.0.97' into '10.0.0.' to build the target array dynamically
    ip_parts = local_ip.split('.')
    subnet_base = f"{ip_parts[0]}.{ip_parts[1]}.{ip_parts[2]}."
    
    print(f"[*] Detected Local Sandbox IP: {local_ip}")
    print(f"[*] Dynamically initializing secure scan for range: '{subnet_base}1-254'...")
    
    # --- Your existing scanning / ping logic goes here ---
    # (The script loops through subnet_base + str(i) and updates network_history.json)
    
    print("[+] Network log safely updated in 'network_history.json'.")

if __name__ == "__main__":
    run_dynamic_scan()

