#!/usr/bin/env python3
import time
import os
import random

CHAKRA_NODES = {
    1: {"name": "Root (Muladhara)", "plexus": "Sacral/Coccygeal", "function": "Grounding Rail"},
    2: {"name": "Sacral (Svadhisthana)", "plexus": "Lumbar Plexus", "function": "Fluid Dynamics"},
    3: {"name": "Solar Plexus (Manipura)", "plexus": "Celiac/Adrenals", "function": "Power Regulator"},
    4: {"name": "Heart (Anahata)", "plexus": "Cardiac Plexus", "function": "System Buffer"},
    5: {"name": "Throat (Vishuddha)", "plexus": "Cervical Plexus", "function": "Command Protocol"},
    6: {"name": "Third Eye (Ajna)", "plexus": "Carotid Plexus", "function": "Render Engine"},
    7: {"name": "Crown (Sahasrara)", "plexus": "Cerebral Cortex", "function": "Core Interface"}
}

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_status_bar(percentage, width=20):
    filled = int(width * percentage / 100)
    bar = "█" * filled + "░" * (width - filled)
    return f"[{bar}] {percentage:.1f}%"

def run_simulation(frequency_hz=40.0, aligned=False):
    print(f"\n{'[ SYSTEM STATUS: ALIGNED ]' if aligned else '[ SYSTEM STATUS: UNALIGNED ]'}")
    print(f"Injecting Core Signal: {frequency_hz} Hz Gamma-Band...\n")
    print(f"{'NODE ID':<10} | {'NODE SYSTEM LAYER':<28} | {'THERMAL LOAD':<15} | {'SYSTEM CAPACITY'}")
    print("-" * 75)
    
    total_thermal_load = 0.0
    total_capacity_drain = 0.0
    
    for node_id, data in CHAKRA_NODES.items():
        time.sleep(0.25)
        
        if aligned:
            thermal_modifier = random.uniform(1.0, 1.8)
            load_percentage = (frequency_hz * thermal_modifier) / 2.5
            capacity_drain = load_percentage * 0.4
        else:
            thermal_modifier = random.uniform(3.5, 5.5) if node_id in [3, 6, 7] else random.uniform(1.2, 2.0)
            load_percentage = (frequency_hz * thermal_modifier)
            capacity_drain = load_percentage * 1.2
            
        if load_percentage > 100.0: load_percentage = 100.0
        if capacity_drain > 100.0: capacity_drain = 100.0
            
        total_thermal_load += load_percentage
        total_capacity_drain += capacity_drain
        
        status_color = "\033[92m" if aligned else ("\033[91m" if load_percentage > 70 else "\033[93m")
        reset_color = "\033[0m"
        
        print(f"Node {node_id:<4} | {data['name']:<28} | {status_color}{load_percentage:6.1f}°C{reset_color}      | {render_status_bar(capacity_drain)}")

    return total_thermal_load / 7, total_capacity_drain / 7

def main():
    clear_terminal()
    print("=" * 75)
    print("          NEBUCHADNEZZAR MARK VI: NEURAL LOAD BALANCER CORE ENGINE          ")
    print("=" * 75)
    
    unaligned_thermal, unaligned_drain = run_simulation(frequency_hz=40.0, aligned=False)
    
    print("\n" + "=" * 75)
    print("CRITICAL ALERT: Hardware threshold approaching melt phase.")
    print("Initiating bottom-up alignment sequence to secure the pipeline...")
    print("=" * 75)
    
    for i in range(3, 0, -1):
        print(f"Synchronizing biometric carrier waves in {i}...")
        time.sleep(1)
        
    clear_terminal()
    print("=" * 75)
    print("          NEBUCHADNEZZAR MARK VI: NEURAL LOAD BALANCER CORE ENGINE          ")
    print("=" * 75)
    
    aligned_thermal, aligned_drain = run_simulation(frequency_hz=40.0, aligned=True)
    
    print("\n" + "=" * 75)
    print("SIMULATION COMPARISON REPORT")
    print("=" * 75)
    print(f"Unaligned Avg Thermal Stress:  {unaligned_thermal:.2f}°C")
    print(f"Aligned Avg Thermal Stress:    {aligned_thermal:.2f}°C (Drop of {unaligned_thermal - aligned_thermal:.2f}°C)")
    print("-" * 75)
    print(f"Unaligned System Core Drain:   {unaligned_drain:.2f}%")
    print(f"Aligned System Core Drain:     {aligned_drain:.2f}% (Efficiency gain of {unaligned_drain - aligned_drain:.2f}%)")
    print("=" * 75)
    if aligned_drain < 30.0:
        print("\033[92mSTATUS: Neural structural integrity nominal. Hardware melt averted.\033[0m\n")

if __name__ == "__main__":
    main()
