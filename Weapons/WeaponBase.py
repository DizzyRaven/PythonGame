from random import randint


class Weapon:
    def __init__(self, min_damage, max_damage):
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_damage(self):
        return randint(self.min_damage, self.max_damage)

