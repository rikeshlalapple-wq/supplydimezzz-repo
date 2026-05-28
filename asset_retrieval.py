import sys

class AssetRetrievalEngine:
    def __init__(self):
        self.target_items = ["car_keys", "house_keys"]
        self.safety_protocols = {
            "NO_DIRECT_CONTACT": True,
            "NO_UNANNOUNCED_APPEARANCE": True,
            "DOCUMENT_EVERYTHING": True
        }

    def evaluate_strategy(self, strategy_name):
        print(f"\n[!] Evaluating Vector: {strategy_name.upper()}")
        
        if strategy_name == "civil_standby":
            risk_score = 1  # Lowest risk
            legality = "100% Protected"
            success_probability = 85
            action_plan = [
                "1. Locate the non-emergency law enforcement number for the apartment's zip code.",
                "2. Request a 'Civil Standby for retrieval of essential property (vehicle keys).'",
                "3. Meet the officer at a designated staging zone a few blocks away from the apartment.",
                "4. Allow the officer to spearhead the physical approach to the door."
            ]
        elif strategy_name == "third_party_liaison":
            risk_score = 2  # Low risk
            legality = "Legal & Documented"
            success_probability = 70
            action_plan = [
                "1. Coordinate with a legal courier or your family law representative.",
                "2. Have them text/email a structured message: 'Arranging neutral pickup of Rikesh's vehicle keys.'",
                "3. Secure a public, monitored drop-off location."
            ]
        elif strategy_name == "direct_approach":
            risk_score = 10  # EXTREMELY HIGH RISK
            legality = "High risk of new emergency call / violation allegations"
            success_probability = 5
            action_plan = [
                "CRITICAL FAILURE MATRIX: DO NOT EXECUTE.",
                "Showing up unannounced creates an immediate vulnerability for false reporting."
            ]
        else:
            return "Unknown vector."

        self._print_matrix_output(risk_score, legality, success_probability, action_plan)

    def _print_matrix_output(self, risk, legality, success, plan):
        print("-" * 60)
        print(f"RISK LEVEL          : {risk}/10")
        print(f"LEGAL SECURITY      : {legality}")
        print(f"PROBABILITY SUCCESS : {success}%")
        print("-" * 60)
        print("EXECUTION STEPS:")
        for step in plan:
            print(f"  {step}")
        print("=" * 60)

if __name__ == "__main__":
    engine = AssetRetrievalEngine()
    
    # Run the evaluation matrix
    engine.evaluate_strategy("civil_standby")
    engine.evaluate_strategy("third_party_liaison")
    engine.evaluate_strategy("direct_approach")
