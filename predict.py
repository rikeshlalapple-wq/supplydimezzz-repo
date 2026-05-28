import datetime

class OutcomePredictor:
    def __init__(self, history):
        # History is a list of past outcomes: 'declined' or 'filed'
        self.history = history
        self.total_cases = len(history)
        
    def calculate_probabilities(self):
        # Count occurrences
        declined_count = self.history.count('declined')
        filed_count = self.history.count('filed')
        
        # Calculate raw mathematical weight
        p_declined = (declined_count / self.total_cases) * 100
        p_filed = (filed_count / self.total_cases) * 100
        
        return p_declined, p_filed

    def generate_analysis(self, current_status):
        # Update history with today's live operational data
        self.history.append(current_status)
        p_dec, p_fil = self.calculate_probabilities()
        
        print("=" * 50)
        print(f" SUPPLYDIMEZZZ PROBABILITY ENGINE | {datetime.datetime.now().strftime('%M:%S')}")
        print("=" * 50)
        print(f"Total Sample Size Analysed : {len(self.history)} Incidents")
        print(f"Historical Sequence        : {' -> '.join([h.upper() for h in self.history])}")
        print("-" * 50)
        print(f"Probability of DISMISSAL/DECLINE : {p_dec:.2f}%")
        print(f"Probability of PROSECUTION       : {p_fil:.2f}%")
        print("-" * 50)
        
        # Systemic evaluation logic
        if p_dec > 70:
            print("[SYSTEM LOG]: Trend strongly favors systemic decline.")
            print("[ACTION]    : Maintain low profile. Secure physical verification slip.")
        else:
            print("[SYSTEM LOG]: Trend shifting. Keep legal counsel operational.")
        print("=" * 50)

# --- LIVE RUNNING SIMULATION ---
# Inputting your 3 data points: 2 past declines + today's live status
# (Change today_outcome to 'filed' or 'declined' based on what the clerk tells you)

past_history = ['declined', 'declined']
today_outcome = 'declined'  # <-- If you walk out free today, this remains 'declined'

predictor = OutcomePredictor(past_history)
predictor.generate_analysis(today_outcome)
