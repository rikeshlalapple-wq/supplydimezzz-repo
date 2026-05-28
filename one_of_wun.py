#!/usr/bin/env python3
import os

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def run_engine():
    clear_screen()
    print("=" * 60)
    print("          THE 'ONE OF WUN' ZERO-COST DIVERSION ENGINE       ")
    print("=" * 60)
    
    # 1. Hardcoded System Constants (Pure Waste Profit Matrix)
    # 100% Net Profit Spread - Input Cost is $0.00
    COMMODITIES = {
        "A": {"name": "Aluminum (Cans / Catering Pans)", "payout": 1.80, "density_lbs_per_bag": 15.0},
        "B": {"name": "#1 PET Plastic (Beverage)", "payout": 1.46, "density_lbs_per_bag": 12.0},
        "C": {"name": "#2 HDPE Plastic (Bulk Jugs/Oils)", "payout": 0.67, "density_lbs_per_bag": 8.0}
    }
    
    # Legal Safeguard Caps
    DAILY_PLASTIC_CAP_LBS = 100.0
    DAILY_ALUMINUM_CAP_LBS = 100.0

    print("[+] Current Pattern: B2B Commercial Waste Diversion")
    print("    [Input Cost: $0.00 | Partner Benefit: Waste Reduction]")
    print("-" * 60)
    
    try:
        partners = int(input("[+] Number of Active Sourcing Sources/Events: ") or 5)
        avg_lbs_per_source = float(input("[+] Avg Material Weight per Source (lbs) : ") or 15.0)
    except ValueError:
        print("[-] Invalid input. Running with baseline data optimization.")
        partners = 5
        avg_lbs_per_source = 15.0

    # 2. Pattern Recognition and Allocation Logic
    # Assume an even distribution of materials across commercial food/beverage waste
    total_haul_weight = partners * avg_lbs_per_source
    allocated_weight_per_type = total_haul_weight / 3
    
    # Financial Compilation
    daily_revenue = 0
    ledger_lines = []
    
    # Check Aluminum
    al_weight = allocated_weight_per_type
    al_payout = al_weight * COMMODITIES["A"]["payout"]
    daily_revenue += al_payout
    al_status = "COMPLIANT" if al_weight <= DAILY_ALUMINUM_CAP_LBS else "EXCEEDS DAILY CAP"
    
    # Check Plastics (#1 and #2 combined under the plastic transport umbrella)
    total_plastic_weight = allocated_weight_per_type * 2
    pet_payout = allocated_weight_per_type * COMMODITIES["B"]["payout"]
    hdpe_payout = allocated_weight_per_type * COMMODITIES["C"]["payout"]
    daily_revenue += (pet_payout + hdpe_payout)
    plastic_status = "COMPLIANT" if total_plastic_weight <= DAILY_PLASTIC_CAP_LBS else "EXCEEDS DAILY CAP"

    # Timeframe Scaling Projections
    monthly_revenue = daily_revenue * 22  # Assuming 22 operational collection days a month
    quarterly_payout = monthly_revenue * 3

    # Total Volume Estimates (Crushed vs Uncrushed Pattern)
    total_bags_uncrushed = (total_haul_weight / 5.0)  # Loose material is light and bulky
    total_bags_crushed = (allocated_weight_per_type / COMMODITIES["A"]["density_lbs_per_bag"]) + \
                          (allocated_weight_per_type / COMMODITIES["B"]["density_lbs_per_bag"]) + \
                          (allocated_weight_per_type / COMMODITIES["C"]["density_lbs_per_bag"])

    # 3. Telemetry Output Ledger
    print("\n" + "=" * 60)
    print("                 LOGISTICAL PATTERN SYSTEM                  ")
    print("=" * 60)
    print(f"Total Route Generated  : {total_haul_weight:.2f} lbs from {partners} sources")
    print(f" -> Aluminum Allocation: {al_weight:.2f} lbs ({al_status})")
    print(f" -> Plastic Allocation : {total_plastic_weight:.2f} lbs ({plastic_status})")
    print("-" * 60)
    print("                 SPATIAL EFFICIENCY TRACER                  ")
    print("-" * 60)
    print(f" -> Uncrushed Volume   : ~{total_bags_uncrushed:.1f} standard utility bags")
    print(f" -> Crushed Volume     : ~{total_bags_crushed:.1f} optimized dense bags")
    print(f"     [Pattern Notice: Crushing saves {((total_bags_uncrushed - total_bags_crushed)/total_bags_uncrushed)*100:.1f}% storage space]")
    print("-" * 60)
    print("                 FINANCIAL INDEX PROJECTIONS                ")
    print("-" * 60)
    print(f" DAILY REVENUE GROSS   : ${daily_revenue:.2f}")
    print(f" MONTHLY REVENUE INDEX : ${monthly_revenue:.2f}")
    print(f" QUARTERLY PASSIVE YIELD: ${quarterly_payout:.2f} (100% NET PROFIT)")
    print("=" * 60)
    
    # System Compliance Flag
    if al_status != "COMPLIANT" or plastic_status != "COMPLIANT":
        print("\n[!] OPTIMIZATION ALERT: Route volume hits CalRecycle limits.")
        print("    Action: Split hauls into morning/afternoon loops to maintain incognito flow.")
    else:
        print("\n[+] SYSTEM EFFICIENCY: 100% Clean. Route fits standard consumer limits.")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_engine()
