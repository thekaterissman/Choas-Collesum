import random
from Aichaosbrain import AIChaosBrain
from Beast_beastary import BeastBestiary
from Gotcha_fails_system import GotchaFailsSystem
from Modes_manger import ModesManager

def print_welcome():
    """Prints the welcome message and available commands."""
    print("\n\n*** Welcome to THE COLISEUM: CHAOS ETERNAL! ***")
    print("Iron gates groan. Trumpets blast. Your heart syncs to the drum.")
    print("The ground quakes as the arena rips free, floating. You are inside.")
    print("A voice echoes, warm and fierce: 'You're unstoppable! Keep swinging!'")
    print("\nWhat is your will, champion?")
    print("\n--- COMMANDS FROM THE CHAOS QUEENS ---")
    print("  info        - Glimpse your soul. See your status.")
    print("  mode [type] - Bend reality. Switch modes (hunter, survival, pvp, raid).")
    print("  act [action]- Make your move. (e.g., fight, craft, raid).")
    print("  buy [beast] - Tame the stars. Buy a beast (leo_lion, scorpio_sting).")
    print("  ride [beast]- Mount your legend. Ride a beast you own.")
    print("  fail [desc] - Embrace the chaos. Record an epic fail.")
    print("  bully [name]- Summon justice. Report a bully to the Queens.")
    print("  twist       - Dare the AI. Unleash a random twist of fate.")
    print("  quit        - Return to the void. Exit the game.")
    print("-----------------------------------------")


def main():
    """Main game loop."""
    # Initialize game components
    ai_brain = AIChaosBrain()
    ai_brain.load_memory()
    beast_bestiary = BeastBestiary(coins=10)  # Start with a pouch of chaos coins
    gotcha_system = GotchaFailsSystem()
    modes_manager = ModesManager()

    print_welcome()

    while True:
        command_input = input("\n> What's your move, champion? ").lower().strip()
        command = command_input.split()

        if not command:
            continue

        action = command[0]

        if action == "quit":
            print("\nThe roar of the crowd fades into a whisper. Your legend awaits its next chapter.")
            break
        elif action == "info":
            print("\n/// Holographic Status Display ///")
            print(f"  Current Reality: {modes_manager.current_mode.upper()}")
            print(f"  Chaos XP: {modes_manager.xp}")
            print(f"  Coin Purse: {beast_bestiary.coins} coins")
            print(f"  Your Stable: {beast_bestiary.owned_beasts or 'Tragically empty'}")
            print("//////////////////////////////////")
        elif action == "mode":
            if len(command) > 1:
                print(modes_manager.switch_mode(command[1]))
            else:
                print("The Queens demand a mode! Try 'mode hunter' or 'mode survival'.")
        elif action == "act":
            if len(command) > 1:
                # Learn the move before earning XP
                ai_brain.learn_move(command[1])
                print(modes_manager.earn_xp(command[1]))
            else:
                print("An action, champion! What will you do? 'act fight', 'act craft'?")
        elif action == "buy":
            if len(command) > 1:
                print(beast_bestiary.buy_beast(command[1]))
            else:
                print("You can't buy nothing! 'buy leo_lion' to get a friend.")
        elif action == "ride":
            if len(command) > 1:
                print(beast_bestiary.ride_beast(command[1]))
            else:
                print("Ride what? The air? 'ride leo_lion' if you have one.")
        elif action == "fail":
            if len(command) > 1:
                fail_desc = " ".join(command[1:])
                print(gotcha_system.add_fail(fail_desc))
            else:
                print("A fail needs a description! 'fail tripped on a cosmic banana'.")
        elif action == "bully":
            if len(command) > 1:
                bully_name = " ".join(command[1:])
                print(gotcha_system.gotcha_bully(bully_name))
            else:
                print("Name the fiend! 'bully troll123'.")
        elif action == "twist":
            print(ai_brain.throw_twist())
        else:
            print(f"\nThe Chaos Queens tilt their heads. '{command_input}'? That's not a command they recognize.")
            print("They cackle, 'Try 'info' to see what you CAN do, star-stuff.'")

if __name__ == "__main__":
    main()
