class MoralChoice:
    def __init__(self, description, options):
        self.description = description
        self.options = options

    def present_choice(self):
        print(self.description)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option['text']}")

    def get_consequence(self, choice_index):
        return self.options[choice_index]['consequence']
