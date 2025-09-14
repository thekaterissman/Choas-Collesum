import random

class ModesManager:
    def __init__(self):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds

    def switch_mode(self, mode, reputation=0):
        modes = ['hunter', 'survival', 'pvp', 'raid']
        if mode in modes:
            self.current_mode = mode
            message = ""
            if mode == 'survival':
                message = "Survival Mode: Craft vines to blades. XP sticks – no resets!"
            elif mode == 'pvp':
                message = "PvP: Teams self-select. Mix crews, clash in the arena!"
            elif mode == 'raid':
                message = "Raid villages! Steal loot, burn down – haptics make walls crack."
            else: # hunter mode
                message = "Hunter Mode: Self-pick teams. Hunt or be hunted."

            if reputation < -10 and mode == 'hunter':
                message += "\nYou are a known outlaw. Other hunters will be rewarded for your demise."

            return message
        return "Invalid mode – chaos only!"

    def earn_xp(self, action):
        xp_gain = random.randint(10, 50)
        self.xp += xp_gain
        if self.current_mode == 'survival':
            self.shelters.append('new_shelter')  # Build persists
        return f"XP +{xp_gain}! Total: {self.xp}. Boosts Coliseum skills."

    def mix_modes(self, mode1, mode2):
        return f"Mixed: {mode1} + {mode2} = Pure dive! Remake world in 5s."

# Usage: manager = ModesManager(); print(manager.switch_mode('survival')); print(manager.earn_xp('raid'))
