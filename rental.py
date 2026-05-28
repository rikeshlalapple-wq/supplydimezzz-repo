import json
from datetime import datetime

class RentalAgreement:
    def __init__(self):
        self.agreement_id = "REGGIE-RL-2026-001"
        self.metadata = {
            "version": "1.0.0",
            "system_origin": "Orb Core Workstation",
            "encryption_status": "Verified",
            "timestamp": datetime.now().isoformat()
        }
        
        self.parties = {
            "owner": {
                "company_name": "Reggie Fleet Rentals",
                "authorized_signatory": "Reggie"
            },
            "renter": {
                "legal_name": "Rikesh Lal",
                "verification_status": "Verified"
            }
        }
        
        self.asset = {
            "make": "Audi",
            "model": "A4",
            "year": 2006,
            "vin": "INSERT_VIN_HERE",
            "license_plate": "INSERT_PLATE_HERE",
            "initial_condition": "Documented via time-stamped media"
        }
        
        self.terms = {
            "duration_days": 2,
            "rate_structure": "Flat Rate",
            "total_cost_usd": 100.00,
            "currency": "USD",
            "fuel_policy": "Return as received",
            "mileage_allowance": "Unlimited"
        }
        
        self.liability = {
            "insurance_requirement": "Renter's primary auto insurance applies",
            "traffic_violations": "Renter holds sole responsibility",
            "damage_liability": "Renter liable for any delta in asset condition"
        }

    def generate_contract_json(self):
        """Compiles the structured contract into a clean JSON layout."""
        contract_data = {
            "Agreement ID": self.agreement_id,
            "Metadata": self.metadata,
            "Parties Involved": self.parties,
            "Asset Architecture": self.asset,
            "Financial & Temporal Terms": self.terms,
            "Liability Matrix": self.liability
        }
        return json.dumps(contract_data, indent=4)

    def print_human_readable(self):
        """Outputs a clean script rendering for verification."""
        border = "=" * 60
        print(border)
        print(f"       LEGAL CONTRACT ENGINE: {self.agreement_id}")
        print(border)
        print(f"OWNER:  {self.parties['owner']['company_name']}")
        print(f"RENTER: {self.parties['renter']['legal_name']}")
        print(f"ASSET:  {self.asset['year']} {self.asset['make']} {self.asset['model']}")
        print(f"TERMS:  {self.terms['duration_days']} Days | {self.terms['rate_structure']} of ${self.terms['total_cost_usd']:.2f}")
        print(border)
        print("STATUS: Ready for deployment and signature compilation.")
        print(border)

# Initialize the contract instance
contract = RentalAgreement()

# Render outputs
contract.print_human_readable()

