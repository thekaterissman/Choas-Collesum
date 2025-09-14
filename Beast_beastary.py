import random

class BeastBestiary:
    def __init__(self, coins=0):
        self.coins = coins
        self.beasts = {
            'Nemean_Lion': {
                'cost': 2,
                'effect': 'A lion whose golden fur is impervious to attack.'
            },
            'Manticore': {
                'cost': 3,
                'effect': 'A creature with the body of a lion, the wings of a bat, and a tail of venomous spines.'
            },
            'Cretan_Bull': {
                'cost': 4,
                'effect': 'A legendary bull, father of the Minotaur, that breathes fire.'
            },
            'Phoenix': {
                'cost': 5,
                'effect': 'A majestic bird of fire, reborn from ashes, a symbol of eternal life.'
            },
            'Hippogriff': {
                'cost': 10,
                'effect': 'A magical beast with the front half of a giant eagle and the rear half of a horse.',
                'required_reputation': 10
            }
        }
        self.owned_beasts = []

    def buy_beast(self, beast_name, reputation=0):
        if beast_name not in self.beasts:
            return "There is no such beast in the Bestiary."

        beast = self.beasts[beast_name]

        if self.coins < beast['cost']:
            return "You lack the coin for such a magnificent beast, champion. Embark on a quest!"

        if 'required_reputation' in beast and reputation < beast['required_reputation']:
            return f"The {beast_name} deems you unworthy. Your reputation is too low."

        self.coins -= beast['cost']
        self.owned_beasts.append(beast_name)
        return f"Beast acquired: {beast_name}! {beast['effect']}"

    def ride_beast(self, beast_name):
        if beast_name in self.owned_beasts:
            zodiac_boost = random.choice(['The stars of Leo flare brightly!', 'The constellation of Scorpio burns in the sky!', 'The scales of Libra find their balance!'])
            return f"You mount your {beast_name} and ride into the arena! {zodiac_boost}"
        return "You have no beast to ride. Visit the Bestiary!"

# Usage: bestiary = BeastBestiary(10); print(bestiary.buy_beast('Phoenix')); print(bestiary.ride_beast('Phoenix'))
