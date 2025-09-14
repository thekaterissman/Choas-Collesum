import random
import json  # For saving "memories"


class AIChaosBrain:
    def __init__(self):
        self.player_moves = []  # Learns your quirks
        self.fears = ['sandstorm', 'floating_islands', 'dance_or_die', 'zero_g', 'reverse_controls']  # Your nightmares
        self.memory_file = 'chaos_memory.json'  # Persists across runs

    def learn_move(self, move):
        self.player_moves.append(move)
        if len(self.player_moves) > 10:
            self.player_moves = self.player_moves[-10:]  # Keep recent
        self.save_memory()

    def throw_twist(self):
        # The AI gets more aggressive if the player is repetitive
        if len(self.player_moves) > 3 and len(set(self.player_moves[-3:])) == 1:
            move = self.player_moves[-1]
            return f"The AI has seen you '{move}' three times in a row. It yawns, 'Boring.' Suddenly, the arena shifts, and a giant holographic hand descends to flick you across the floor."

        # The AI reacts to specific common moves
        if 'dodge' in self.player_moves[-3:]:  # If you're dodging a lot...
            twist = random.choice(self.fears)
            if twist == 'dance_or_die':
                return "The AI whispers in your ear, its voice like crackling static: 'I see you like to move. Dance for me, champion, or face oblivion. A shield for a show!'"
            elif twist == 'sandstorm':
                return "The AI chuckles. 'You can't dodge the wind.' A sudden, blinding sandstorm engulfs the arena! The haptic suit simulates grit in your teeth. You can either dodge and pray, or try to bury yourself."
            elif twist == 'floating_islands':
                return "The AI decides to change the scenery. 'Let's see how you handle this.' The ground shatters into a hundred floating islands, and gravity flips. Your stomach lurches. Don't fall."
            elif twist == 'zero_g':
                return "The AI hums a tune. 'Time for a change of pace.' Gravity ceases to exist. You are now floating in a zero-g environment. Good luck."
            else: # reverse_controls
                return "The AI gets mischievous. 'Let's play a game.' Your controls are now reversed. Left is right, up is down. Have fun!"
        else:
            # Generic, but still epic, taunts
            taunts = [
                "The AI adapts to your strategy. A basic roar from a Leo constellation echoes in the arena. You feel the rumble in your bones.",
                "The AI projects a star map in your peripheral vision. It highlights your birth sign. 'I know you,' it seems to say.",
                "A shower of harmless, glittering meteors rains down. It's beautiful, but distracting."
            ]
            return random.choice(taunts)

    def save_memory(self):
        memory = {'moves': self.player_moves}
        with open(self.memory_file, 'w') as f:
            json.dump(memory, f)

    def load_memory(self):
        try:
            with open(self.memory_file, 'r') as f:
                memory = json.load(f)
                self.player_moves = memory.get('moves', [])
        except FileNotFoundError:
            pass  # Fresh chaos


# Usage: brain = AIChaosBrain(); brain.load_memory(); print(brain.throw_twist())
