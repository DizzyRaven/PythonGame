from random import randint


class Weapon:
    def __init__(self, min_damage, max_damage):
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_damage(self):
        return randint(self.min_damage, self.max_damage)


class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__(2, 10)

    def get_damage(self):
        rand = randint(1, 2)
        if rand == 1:
            return self.min_damage
        else:
            return self.max_damage



