import random
from Aichaosbrain import AIChaosBrain
from Beast_beastary import BeastBestiary
from Gotcha_fails_system import GotchaFailsSystem
from Modes_manger import ModesManager
from inventory import Inventory
from pocket_universe import PocketUniverse

def print_welcome():
    """Prints the welcome message and available commands."""
    print("\n\n*** Welcome to THE COLISEUM: CHAOS ETERNAL! ***")
    print("Iron gates groan. Trumpets blast. Your heart syncs to the drum.")
    print("The ground quakes as the arena rips free, floating. You are inside.")
    print("A voice echoes, warm and fierce: 'You're unstoppable! Keep swinging!'")
    print("\nWhat is your will, champion?")
    print("\n--- COMMANDS FROM THE CHAOS QUEENS ---")
    print("  info          - Glimpse your soul. See your status.")
    print("  inventory     - Behold your treasures. Check your inventory.")
    print("  mode [type]   - Bend reality. Switch modes (hunter, survival, pvp, raid, build).")
    print("  act [action]  - Make your move. (e.g., fight, craft, raid).")
    print("  --- Build Mode Commands ---")
    print("  view_universe - Look upon your creation. View your pocket universe.")
    print("  build [object]- Shape the void. Create an object in your universe.")
    print("  describe_universe [text] - Define your reality. Describe your universe.")
    print("  ---------------------------")
    print("  buy [beast]   - Tame the stars. Buy a beast (leo_lion, scorpio_sting).")
    print("  ride [beast]  - Mount your legend. Ride a beast you own.")
    print("  fail [desc]   - Embrace the chaos. Record an epic fail.")
    print("  bully [name]  - Summon justice. Report a bully to the Queens.")
    print("  twist         - Dare the AI. Unleash a random twist of fate.")
    print("  quit          - Return to the void. Exit the game.")
    print("-----------------------------------------")


def main():
    """Main game loop."""
    # Initialize game components
    ai_brain = AIChaosBrain()
    ai_brain.load_memory()
    beast_bestiary = BeastBestiary(coins=10)
    gotcha_system = GotchaFailsSystem()
    modes_manager = ModesManager()
    inventory = Inventory()
    pocket_universe = PocketUniverse()

    print_welcome()

    while True:
        command_input = input("\n> What's your move, champion? ").lower().strip()
        command = command_input.split()

        if not command:
            continue

        action = command[0]
        args = command[1:]

        if action == "quit":
            print("\nThe roar of the crowd fades into a whisper. Your legend awaits its next chapter.")
            break
        elif action == "info":
            print("\n/// Holographic Status Display ///")
            print(f"  Current Reality: {modes_manager.current_mode.upper()}")
            print(f"  Chaos XP: {modes_manager.xp}")
            print(f"  Coin Purse: {beast_bestiary.coins} coins")
            print(f"  Your Stable: {beast_bestiary.owned_beasts or 'Tragically empty'}")
            print(f"  Inventory: {len(inventory.get_items())} items")
            print("//////////////////////////////////")
        elif action == "inventory":
            print(inventory.display_inventory())
        elif action == "mode":
            if args:
                print(modes_manager.switch_mode(args[0]))
            else:
                print("The Queens demand a mode! Try 'mode build'.")
        elif action == "act":
            if modes_manager.current_mode == 'build':
                print("You are in build mode. Actions like 'act' have no meaning here. Try 'build' or 'describe_universe'.")
            elif args:
                ai_brain.learn_move(args[0])
                print(modes_manager.earn_xp(args[0], inventory))
            else:
                print("An action, champion! What will you do? 'act fight', 'act craft'?")

        # Build Mode Commands
        elif action == "view_universe":
            print(pocket_universe.display_universe())
        elif action == "build":
            if modes_manager.current_mode != 'build':
                print("You must be in 'build' mode to shape your universe. Try 'mode build'.")
            elif args:
                object_name = " ".join(args)
                print(pocket_universe.add_object(object_name))
            else:
                print("Build what? You must name your creation. 'build a floating castle'.")
        elif action == "describe_universe":
            if modes_manager.current_mode != 'build':
                print("You must be in 'build' mode to shape your universe. Try 'mode build'.")
            elif args:
                description = " ".join(args)
                print(pocket_universe.set_description(description))
            else:
                print("Describe it how? 'describe_universe a realm of endless twilight'.")

        elif action == "buy":
            if args:
                print(beast_bestiary.buy_beast(args[0]))
            else:
                print("You can't buy nothing! 'buy leo_lion' to get a friend.")
        elif action == "ride":
            if args:
                print(beast_bestiary.ride_beast(args[0]))
            else:
                print("Ride what? The air? 'ride leo_lion' if you have one.")
        elif action == "fail":
            if args:
                fail_desc = " ".join(args)
                print(gotcha_system.add_fail(fail_desc))
            else:
                print("A fail needs a description! 'fail tripped on a cosmic banana'.")
        elif action == "bully":
            if args:
                bully_name = " ".join(args)
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
