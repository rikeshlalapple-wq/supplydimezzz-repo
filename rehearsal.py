import sys
import time

class CourtroomSimulation:
    def __init__(self):
        self.department = "60"
        self.charges = ["PC 243.4(e)(1)", "PC 243(e)(1)"]
        self.state_notebook = {
            "NOMAD_STANCE": "Absolute emotional detachment. Clear eyes. No reactionary expressions.",
            "GOLDEN_RULE": "Do not speak to anyone about the facts of the case. Only state your identity.",
            "LEGAL_RIGHT": "Request a public defender immediately if private counsel is not present."
        }

    def simulate_input(self, scenario_type):
        print(f"\n[!] Initializing Rehearsal Script for Scenario: {scenario_type.upper()}")
        time.sleep(0.5)
        
        if scenario_type == "declined":
            self._execute_declined_protocol()
        elif scenario_type == "filed":
            self._execute_filed_protocol()
        else:
            print("[-] Unknown variable input.")

    def _execute_declined_protocol(self):
        print("-" * 50)
        print("SCRIPT RUN TIME: CASE NOT ON CALENDAR / DECLINED")
        print("-" * 50)
        print(f"1. Approach the Clerk Window for Department {self.department}.")
        print("2. REHEARSAL DIALOGUE:")
        print("   You: 'Hi, my name is Rikesh Lal. I am here for a 1:30 PM appearance on a bail bond.'")
        print("3. IF CLERK SAYS: 'Charges are not filed / You are free to go.'")
        print("   Action: Ask for a physical 'Bail Bond Appearance Verification' slip or receipt.")
        print("   You: 'May I please have a minute order or appearance verification for my bondsman?'")
        print("4. EXIT PROTOCOL: Leave the building immediately. Text the bondsman a photo of the slip. Do not linger.")
        print(f"\n[Core Workstation Note]: {self.state_notebook['NOMAD_STANCE']}")

    def _execute_filed_protocol(self):
        print("-" * 50)
        print("SCRIPT RUN TIME: ARRAIGNMENT IS ACTIVE")
        print("-" * 50)
        print("1. Take a seat quietly in the gallery. Wait for 'Lal, Rikesh' to be called.")
        print("2. REHEARSAL DIALOGUE WITH THE PUBLIC DEFENDER / COUNSEL:")
        print("   Counsel: 'Mr. Lal, I have the D.A. packet.'")
        print("   You: 'Thank you. I want to enter a Not Guilty plea today, look at discovery, and protect my release status.'")
        print("3. REHEARSAL DIALOGUE WITH THE JUDGE (If addressing you directly):")
        print("   Judge: 'Mr. Lal, do you understand your rights?'")
        print("   You: 'Yes, Your Honor.'")
        print("4. THE CRITICAL RESTRAINT:")
        print("   * If the D.A. or Judge mentions the details of your wife's statements, your jaw stays locked. *")
        print("   * You do not correct them. You do not explain context. You say absolutely nothing to defend yourself out loud. *")
        print(f"\n[Core Workstation Note]: {self.state_notebook['GOLDEN_RULE']}")

if __name__ == "__main__":
    sim = CourtroomSimulation()
    sim.simulate_input("declined")
    print("\n" + "="*60 + "\n")
    sim.simulate_input("filed")
