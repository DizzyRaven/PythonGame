from random import randint


class Weapon:
    def __init__(self, min_damage, max_damage):
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_damage(self):
        return randint(self.min_damage, self.max_damage)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(5,7)

    def get_damage(self):
        return super(Sword, self). get_damage()

class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__(2, 10)

    def get_damage(self):
        rand = randint(1, 2)
        if rand == 1:
            return self.min_damage
        else:
            return self.max_damage

class Bow(Weapon):
    def __init__(self):
        super(Bow, self).__init__()




