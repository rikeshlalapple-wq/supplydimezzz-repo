#!/usr/bin/env python3
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_pro_dashboard():
    clear_screen()
    print("=" * 65)
    print("             B2B ASSET RECOVERY & LOGISTICS CONSOLE          ")
    print("=" * 65)
    print("[STATUS]: Active Point-of-Origin Bins | Input Sourcing Cost: $0.00")
    print("-" * 65)

    # 1. LIVE COMMODITY MATRIX (MATCHED TO SIGNBOARD)
    COMMODITIES = {
        "Aluminum": {"payout": 1.80, "crush_ratio": 5.0},
        "PET_Plastic": {"payout": 1.46, "crush_ratio": 4.0},
        "PS_Plastic": {"payout": 5.45, "crush_ratio": 1.0}
    }
    
    DAILY_PLASTIC_LIMIT = 100.0
    DAILY_ALUMINUM_LIMIT = 100.0

    # 2. INPUT COLLECTION
    try:
        active_bins = int(input("[+] Enter number of active B2B collection bins on route: ") or 6)
        avg_weight_per_bin = float(input("[+] Enter estimated weight per bin collected (lbs): ") or 20.0)
    except ValueError:
        print("[-] Invalid input formatting. Defaulting to baseline metrics.")
        active_bins = 6
        avg_weight_per_bin = 20.0

    # 3. PATTERN SPLIT (40% Al, 40% PET, 20% #6 PS)
    total_payload_weight = active_bins * avg_weight_per_bin
    al_weight = total_payload_weight * 0.40
    pet_weight = total_payload_weight * 0.40
    ps_weight = total_payload_weight * 0.20
    total_combined_plastic = pet_weight + ps_weight

    # 4. REVENUE EXTRACTION ENGINE
    al_gross = al_weight * COMMODITIES["Aluminum"]["payout"]
    pet_gross = pet_weight * COMMODITIES["PET_Plastic"]["payout"]
    ps_gross = ps_weight * COMMODITIES["PS_Plastic"]["payout"]
    total_daily_net_profit = al_gross + pet_gross + ps_gross
    
    monthly_yield = total_daily_net_profit * 22
    quarterly_yield = monthly_yield * 3

    # 5. SPATIAL CALCULATIONS
    loose_bags = total_payload_weight / 5.0
    crushed_bags = (al_weight / (5.0 * COMMODITIES["Aluminum"]["crush_ratio"])) + \
                    (pet_weight / (5.0 * COMMODITIES["PET_Plastic"]["crush_ratio"])) + \
                    (ps_weight / (5.0 * COMMODITIES["PS_Plastic"]["crush_ratio"]))

    # 6. PRINT MANIFEST TELEMETRY
    clear_screen()
    print("=" * 65)
    print("                  ROUTE SHIPMENT MANIFEST                    ")
    print("=" * 65)
    print(f"Total Network Cargo Weight : {total_payload_weight:.2f} lbs")
    print(f"Active Point-of-Origin Bins: {active_bins} units processed")
    print("-" * 65)
    print("              COMMODITY WEIGHT & LEGAL MATRIX                ")
    print("-" * 65)
    
    al_status = "COMPLIANT" if al_weight <= DAILY_ALUMINUM_LIMIT else "EXCEEDS DAILY MAX"
    plastic_status = "COMPLIANT" if total_combined_plastic <= DAILY_PLASTIC_LIMIT else "EXCEEDS DAILY MAX"
    
    print(f" -> Aluminum Payload       : {al_weight:.2f} lbs | [{al_status}]")
    print(f" -> Combined Plastic Load  : {total_combined_plastic:.2f} lbs | [{plastic_status}]")
    print(f"    (*Breakdown: {pet_weight:.2f} lbs #1 PET | {ps_weight:.2f} lbs #6 PS)")
    print("-" * 65)
    print("                 VOLUME DENSITY MONITOR                    ")
    print("-" * 65)
    print(f" -> Loose Cargo Volume     : ~{loose_bags:.1f} standard transport bags")
    print(f" -> Mechanized Dense Volume: ~{crushed_bags:.1f} optimized cargo bags")
    print(f" -> Cargo Space Saved      : {((loose_bags - crushed_bags) / loose_bags) * 100:.1f}%")
    print("-" * 65)
    print("                 SECURE LEDGER CASH FLOW                    ")
    print("-" * 65)
    print(f" DAILY TRANSACTION GROSS   : ${total_daily_net_profit:.2f}")
    print(f" PROJECTED MONTHLY INDEX   : ${monthly_yield:.2f}")
    print(f" PROJECTED QUARTERLY YIELD : ${quarterly_yield:.2f} [100% NET PROFIT]")
    print("=" * 65)

    if al_status != "COMPLIANT" or plastic_status != "COMPLIANT":
        print("\n[!] CRITICAL SYSTEM ALERT: Manifest violates CalRecycle weight caps.")
        print("    LOGISTICAL ADJUSTMENT: Split route to maintain clean standard logs.")
    else:
        print("\n[+] SYSTEM STABILITY: Optimal. Haul fits standard consumer limits.")
    print("=" * 65 + "\n")

if __name__ == "__main__":
    run_pro_dashboard()
