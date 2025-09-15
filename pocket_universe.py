class PocketUniverse:
    def __init__(self):
        self.description = "A swirling nebula of potential, waiting for a creator's touch."
        self.objects = []

    def set_description(self, new_description):
        """Sets a new description for the universe."""
        self.description = new_description
        return f"The very fabric of your universe shifts. It is now: {self.description}"

    def add_object(self, object_name):
        """Adds an object to the universe."""
        if object_name in self.objects:
            return f"A '{object_name}' already exists in your universe. Try building something new!"
        self.objects.append(object_name)
        return f"With a thought, you conjure a '{object_name}' into existence."

    def display_universe(self):
        """Returns a formatted string describing the universe."""
        display_str = "\n*** Your Pocket Universe ***\n"
        display_str += f"Description: {self.description}\n"
        display_str += "----------------------------\n"

        if not self.objects:
            display_str += "It is vast and empty, awaiting your creations.\n"
        else:
            display_str += "Objects within:\n"
            for obj in self.objects:
                display_str += f"  - A shimmering {obj}\n"

        display_str += "**************************"
        return display_str
