import os, sys, subprocess
class OrbCircleController:
    def run_dashboard(self):
        while True:
            print("="*50)
            print("        ORB WORKSTATION: THE UNIFIED CIRCLE")
            print("="*50)
            print(" [1] Node Alpha : Business & Arbitrage Engine")
            print(" [2] Node Civil : Act 2 Litigation Registry")
            print(" [3] Node Federal: Act 3 Forensic Audit Chain")
            print(" [4] Suspend Session")
            print("-"*50)
            choice = input("Select active circle node [1-4]: ").strip()
            if choice == "1": subprocess.run(["python", os.path.expanduser("~/orb_core_workstation/universe_engine.py")])
            elif choice == "2": subprocess.run(["python", os.path.expanduser("~/orb_core_workstation/civil_engine.py")])
            elif choice == "3": subprocess.run(["python", os.path.expanduser("~/orb_core_workstation/federal_engine.py")])
            elif choice == "4": break
if __name__ == "__main__":
    OrbCircleController().run_dashboard()
