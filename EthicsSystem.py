from MoralChoice import MoralChoice

class EthicsSystem:
    def __init__(self):
        self.reputation = 0  # Neutral reputation
        self.laws = {
            'theft': {'description': "Do not steal.", 'penalty': -2},
            'assault': {'description': "Do not harm the innocent.", 'penalty': -5},
            'treason': {'description': "Respect the Chaos Queens.", 'penalty': -10}
        }
        self.moral_choices = []

    def get_reputation_title(self):
        if self.reputation > 10:
            return "Saint"
        elif self.reputation > 5:
            return "Honorable"
        elif self.reputation < -10:
            return "Scourge"
        elif self.reputation < -5:
            return "Dishonorable"
        else:
            return "Neutral"

    def law_check(self, action):
        if action in self.laws:
            return self.laws[action]['penalty']
        return 0

    def apply_penalty(self, penalty):
        self.reputation += penalty
