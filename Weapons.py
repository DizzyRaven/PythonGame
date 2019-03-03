from random import randint


class Weapon:
    def __init__(self, min_damage, max_damage):
        self.min_damage = min_damage
        self.max_damage = max_damage

    def get_damage(self):
        return randint(self.min_damage, self.max_damage)

class Sword(Weapon):
    def __init__(self):
        super(Sword, self).__init__(5, 7)


    def get_damage(self):
       baseDamage=  super(Sword, self).get_damage()
       random = randint(0,100)
       if random<11 :
           return baseDamage*2
       else:
           return baseDamage

