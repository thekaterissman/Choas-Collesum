from Aichaosbrain import AIChaosBrain
from Beast_beastary import BeastBestiary
from Gotcha_fails_system import GotchaFailsSystem
from Modes_manager import ModesManager
from HapticSystem import HapticSystem
import random

class GameEngine:
    def __init__(self):
        self.ai_brain = AIChaosBrain()
        self.bestiary = BeastBestiary()
        self.gotcha_system = GotchaFailsSystem()
        self.modes_manager = ModesManager()
        self.haptic_system = HapticSystem()
        self.player = {'health': 100, 'position': (0, 0)}

    def start(self):
        print("Welcome to The Coliseum: Chaos Eternal!")
        print(self.haptic_system.ground_rumble())
        # Game loop will go here
        while True:
            print("\nWhat do you want to do?")
            print("1. Get an AI twist")
            print("2. Buy a beast (you have {} coins)".format(self.bestiary.coins))
            print("3. Report a bully")
            print("4. Switch mode")
            print("5. Do a quest (earn coins)")
            print("6. Exit")

            choice = input("> ")

            if choice == '1':
                print(self.ai_brain.throw_twist())
            elif choice == '2':
                beast_name = input("Enter beast name (e.g., leo_lion): ")
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
                print("Thanks for playing!")
                break
            else:
                print("Invalid choice. Try again.")

if __name__ == '__main__':
    engine = GameEngine()
    engine.start()
