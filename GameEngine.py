from Aichaosbrain import AIChaosBrain
from Beast_beastary import BeastBestiary
from Gotcha_fails_system import GotchaFailsSystem
from Modes_manager import ModesManager
from HapticSystem import HapticSystem
from EthicsSystem import EthicsSystem
from MoralChoice import MoralChoice
import random

class GameEngine:
    def __init__(self):
        self.ai_brain = AIChaosBrain()
        self.bestiary = BeastBestiary()
        self.gotcha_system = GotchaFailsSystem()
        self.modes_manager = ModesManager()
        self.haptic_system = HapticSystem()
        self.ethics_system = EthicsSystem()
        self.player = {'health': 100, 'position': (0, 0)}
        self._populate_moral_choices()

    def _populate_moral_choices(self):
        choice1 = MoralChoice(
            "A merchant drops a bag of coins. What do you do?",
            [
                {'text': "Return the coins.", 'consequence': {'reputation': 2}},
                {'text': "Keep the coins.", 'consequence': {'reputation': -2, 'coins': 10}}
            ]
        )
        self.ethics_system.moral_choices.append(choice1)

    def start(self):
        print("Hark, warrior, and welcome to the Coliseum, where chaos reigns eternal!")
        print(self.haptic_system.ground_rumble())
        # Game loop will go here
        while True:
            print("\n---")
            print(f"Your Reputation: {self.ethics_system.get_reputation_title()} ({self.ethics_system.reputation})")
            print("What is your will, champion?")
            print("1. Consult the Oracle (AI twist)")
            print("2. Visit the Bestiary (buy a beast, you have {} coins)".format(self.bestiary.coins))
            print("3. Invoke the Queens' Justice (report a bully)")
            print("4. Choose your fate (switch mode)")
            print("5. Embark on a Quest (earn coins)")
            print("6. Do a good deed (increase reputation)")
            print("7. Steal from a merchant (violates the law)")
            print("8. Face a moral dilemma")
            print("9. Leave the arena")

            choice = input("> ")

            if choice == '1':
                print(self.ai_brain.throw_twist())
            elif choice == '2':
                beast_name = input("Enter beast name (e.g., Nemean_Lion): ")
                print(self.bestiary.buy_beast(beast_name))
            elif choice == '3':
                bully_name = input("Enter bully's name: ")
                print(self.gotcha_system.gotcha_bully(bully_name))
            elif choice == '4':
                mode_name = input("Enter mode (hunter, survival, pvp, raid): ")
                print(self.modes_manager.switch_mode(mode_name))
            elif choice == '5':
                quest_coins = random.randint(1, 5)
                self.bestiary.coins += quest_coins
                print(f"You completed a quest and earned {quest_coins} coins!")
            elif choice == '6':
                self.ethics_system.reputation += 1
                print("You helped a citizen in need. Your reputation increases.")
            elif choice == '7':
                penalty = self.ethics_system.law_check('theft')
                if penalty != 0:
                    self.ethics_system.apply_penalty(penalty)
                    print(f"You stole from a merchant and were caught! Your reputation suffers a penalty of {penalty}.")
                else:
                    # This should not happen with the current implementation, but it's good practice to handle it.
                    print("You stole from a merchant, but it seems there is no law against it... for now.")
            elif choice == '8':
                if not self.ethics_system.moral_choices:
                    print("The gods are silent for now. No dilemmas to face.")
                else:
                    moral_choice = random.choice(self.ethics_system.moral_choices)
                    moral_choice.present_choice()
                    player_choice = int(input("> ")) - 1
                    consequence = moral_choice.get_consequence(player_choice)
                    if 'reputation' in consequence:
                        self.ethics_system.reputation += consequence['reputation']
                        print(f"Your reputation has changed by {consequence['reputation']}.")
                    if 'coins' in consequence:
                        self.bestiary.coins += consequence['coins']
                        print(f"You have gained {consequence['coins']} coins.")
            elif choice == '9':
                print("You leave the arena, your legend echoing in the halls of the Coliseum.")
                break
            else:
                print("Your command is not understood in this realm. Try again.")

if __name__ == '__main__':
    engine = GameEngine()
    engine.start()
