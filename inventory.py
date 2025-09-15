class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item_name):
        """Adds an item to the inventory."""
        self.items.append(item_name)
        return f"You have acquired a new item: {item_name}"

    def get_items(self):
        """Returns the list of items in the inventory."""
        return self.items

    def display_inventory(self):
        """Returns a formatted string of the inventory contents."""
        if not self.items:
            return "Your inventory is empty. Go find some loot!"

        inventory_str = "--- Your Inventory ---\n"
        # Using a dictionary to count item occurrences
        item_counts = {}
        for item in self.items:
            item_counts[item] = item_counts.get(item, 0) + 1

        for item, count in item_counts.items():
            if count > 1:
                inventory_str += f"- {item} (x{count})\n"
            else:
                inventory_str += f"- {item}\n"
        inventory_str += "--------------------"
        return inventory_str
