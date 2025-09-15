import random

class ModesManager:
    def __init__(self):
        self.current_mode = 'hunter'
        self.xp = 0
        self.shelters = []  # Persist builds

    def switch_mode(self, mode):
        modes = ['hunter', 'survival', 'pvp', 'raid', 'build']
        if mode in modes:
            self.current_mode = mode
            if mode == 'survival':
                return "The world warps. You're in SURVIVAL mode now. Craft vines to blades, find healing berries. The XP you earn here is yours forever."
            elif mode == 'pvp':
                return "A blood-red sky dawns. It's PLAYER vs. PLAYER. Choose your crew, or go it alone. The Chaos Queens are watching."
            elif mode == 'raid':
                return "You feel the ground tremble. It's a RAID. Hit villages like thunder, steal their loot, and burn it all down. The haptic feedback will make you flinch when a wall cracks."
            elif mode == 'build':
                return "You retreat into the quiet of your own mind. You are in BUILD mode. Here, you can shape your own pocket universe. The only limit is your imagination."
            else: # hunter mode
                return "The hunt is on. You are in HUNTER mode. Self-select your teams. Hunt, or be hunted."
        return "The Chaos Queens laugh. 'That's not a mode, champion! Try 'hunter', 'survival', 'pvp', 'raid', or 'build'.'"

    def earn_xp(self, action, inventory):
        """Earns XP and potentially items based on the action and mode."""
        xp_gain = random.randint(10, 50)
        self.xp += xp_gain

        action_message = f"Your legend grows! You've gained {xp_gain} Chaos XP for your {action}. Your total XP is now {self.xp}. This power will serve you well in the Coliseum."

        if self.current_mode == 'survival':
            self.shelters.append('new_shelter')  # Build persists
            if action == 'craft':
                item = "a roughly-made plasma blade"
                inventory.add_item(item)
                action_message += f"\nYou crafted {item} and added it to your inventory."

        if self.current_mode == 'raid' and action == 'raid':
            item = "a handful of stolen star-crystals"
            inventory.add_item(item)
            action_message += f"\nYou plundered {item} from the village!"

        return action_message

    def mix_modes(self, mode1, mode2):
        return f"The universe shatters and reforms! You've mixed {mode1.upper()} and {mode2.upper()}! Get ready for pure, unadulterated chaos. The world will remake itself in 5... 4... 3..."

# Usage: manager = ModesManager(); print(manager.switch_mode('survival')); print(manager.earn_xp('raid'))
