import random
from Aichaosbrain import AIChaosBrain
from Beast_beastary import BeastBestiary
from Gotcha_fails_system import GotchaFailsSystem
from Modes_manger import ModesManager

def print_welcome():
    """Prints the welcome message and available commands."""
    print("\nWelcome to The Coliseum: Chaos Eternal!")
    print("The haptic suit hums with life. The roar of the crowd is deafening.")
    print("What will you do?")
    print("\nAvailable commands:")
    print("  info        - Show your current status")
    print("  mode [mode] - Switch game mode (hunter, survival, pvp, raid)")
    print("  act [action]- Perform an action (e.g., fight, craft, raid)")
    print("  buy [beast] - Buy a beast (e.g., leo_lion, scorpio_sting)")
    print("  ride [beast]- Ride one of your beasts")
    print("  fail [desc] - Record an epic fail")
    print("  bully [name]- Report a bully")
    print("  twist       - Let the AI throw a twist")
    print("  quit        - Exit the game")

def main():
    """Main game loop."""
    # Initialize game components
    ai_brain = AIChaosBrain()
    ai_brain.load_memory()
    beast_bestiary = BeastBestiary(coins=10) # Start with some coins
    gotcha_system = GotchaFailsSystem()
    modes_manager = ModesManager()

    print_welcome()

    while True:
        command = input("\n> ").lower().strip().split()

        if not command:
            continue

        action = command[0]

        if action == "quit":
            print("The roar of the crowd fades. Until next time, champion.")
            break
        elif action == "info":
            print(f"\n--- Player Status ---")
            print(f"Current Mode: {modes_manager.current_mode}")
            print(f"XP: {modes_manager.xp}")
            print(f"Coins: {beast_bestiary.coins}")
            print(f"Owned Beasts: {beast_bestiary.owned_beasts}")
            print(f"---------------------")
        elif action == "mode":
            if len(command) > 1:
                print(modes_manager.switch_mode(command[1]))
            else:
                print("Usage: mode [hunter|survival|pvp|raid]")
        elif action == "act":
            if len(command) > 1:
                print(modes_manager.earn_xp(command[1]))
            else:
                print("Usage: act [action]")
        elif action == "buy":
            if len(command) > 1:
                print(beast_bestiary.buy_beast(command[1]))
            else:
                print("Usage: buy [beast_name]")
        elif action == "ride":
            if len(command) > 1:
                print(beast_bestiary.ride_beast(command[1]))
            else:
                print("Usage: ride [beast_name]")
        elif action == "fail":
            if len(command) > 1:
                fail_desc = " ".join(command[1:])
                print(gotcha_system.add_fail(fail_desc))
            else:
                print("Usage: fail [description]")
        elif action == "bully":
            if len(command) > 1:
                bully_name = " ".join(command[1:])
                print(gotcha_system.gotcha_bully(bully_name))
            else:
                print("Usage: bully [name]")
        elif action == "twist":
            print(ai_brain.throw_twist())
        else:
            print("Unknown command. The Chaos Queens mock your confusion.")
            print_welcome()

if __name__ == "__main__":
    main()
