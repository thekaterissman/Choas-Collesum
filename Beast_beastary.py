import random

class BeastBestiary:
    def __init__(self, coins=0):
        self.coins = coins
        self.beasts = {
            'leo_lion': {'cost': 1, 'effect': 'A lion made of stars roars, and its cry shakes your very soul. Haptic thunder rolls through you.'},
            'scorpio_sting': {'cost': 1, 'effect': 'A scorpion of pure energy materializes, its tail crackling. You feel a cosmic slap, a buzz in your hand.'},
            'taurus_bull': {'cost': 2, 'effect': 'A great bull of plasma charges forth. The ground quakes beneath your feet.'},
            'phoenix': {'cost': 5, 'effect': 'A phoenix of pure fire rises from a pool of plasma. A warm, brilliant glow envelops you.'},
            'knight_mount': {'cost': 10, 'effect': 'You summon a legendary Knight of the Chaos Queens. You can feel the power radiating from their plasma armor. The Chaos Crown is within your reach!'}
        }
        self.owned_beasts = []

    def buy_beast(self, beast_name):
        if beast_name in self.beasts and self.coins >= self.beasts[beast_name]['cost']:
            self.coins -= self.beasts[beast_name]['cost']
            self.owned_beasts.append(beast_name)
            return f"A pact is sealed! The {beast_name} is now yours. {self.beasts[beast_name]['effect']} The stars of the Sons flare in acknowledgement!"
        elif beast_name not in self.beasts:
            return f"The Chaos Queens look confused. '{beast_name}'? They do not know of such a creature. Are you sure you spelled it right?"
        else:
            return "Your coin purse is too light, champion. The stars do not answer to empty pockets. Go raid a village, or prove your worth in the arena!"

    def ride_beast(self, beast_name):
        if beast_name in self.owned_beasts:
            zodiac_boost = random.choice(['Leo roars with pride!', 'Scorpio stings with venomous speed!', 'Libra weighs the battle in your favor!', 'Taurus charges with unstoppable force!'])
            return f"You leap onto your {beast_name}! {zodiac_boost} You feel the jolt of cosmic power course through your veins. Onward, to glory!"
        return "You try to ride a beast you do not own. The air shimmers and you fall on your face. Perhaps you should buy one first."

# Usage: bestiary = BeastBestiary(5); print(bestiary.buy_beast('leo_lion')); print(bestiary.ride_beast('leo_lion'))
