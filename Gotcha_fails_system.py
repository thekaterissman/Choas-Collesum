import random

class GotchaFailsSystem:
    def __init__(self):
        self.fails_reel = []
        self.gotcha_list = []

    def add_fail(self, fail_desc):
        self.fails_reel.append(fail_desc)
        sound = random.choice(['a sad trombone solo', 'the Wilhelm scream', 'a rubber chicken squawk', 'cosmic chimes of failure', 'a wet fart noise that echoes through the cosmos'])
        replay_style = random.choice(['in dramatic slow-motion', 'on a loop with flashing lights', 'with a laugh track from the Chaos Queens themselves'])

        return f"*** TOTAL FAILS REEL ***\nA new epic fail has been recorded for all eternity! '{fail_desc}' is now immortalized, replaying {replay_style} accompanied by {sound}. The crowd roars with laughter!"

    def gotcha_bully(self, bully_name):
        punishments = [
            'a giant, holographic pie materializes and SPLATS against their face, dripping virtual cream everywhere',
            'their avatar is forced into a chicken suit and made to dance the Funky Chicken for a full minute',
            'a personal, localized raincloud appears over their head, complete with tiny lightning bolts of shame',
            'their weapon is replaced with a pool noodle for the next five minutes',
            'their face is plastered on the arena jumbotron with a neon sign that says "I <3 THE CHAOS QUEENS"'
        ]
        punishment = random.choice(punishments)
        self.gotcha_list.append(f"{bully_name}: {punishment}")
        return f"*** CHAOS QUEENS' GOTCHA LIST ***\nThe list glows with righteous fury! {bully_name.upper()} has earned their comeuppance! Suddenly, {punishment}. Bullies beware!"

# Usage: system = GotchaFailsSystem(); print(system.add_fail('epic faceplant')); print(system.gotcha_bully('troll123'))
