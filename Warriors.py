class WarriorBase:

    def __init__(self, weapon, name):
        self.name = name
        self.weapon = weapon
        self.hp = 100

    def kick(self):
        pass


class Orc(WarriorBase):

    def __init__(self, weapon, name):
        super(Orc, self).__init__(weapon, name)
        self.hp = self.hp + 20

    def kick(self):
        return self.weapon.get_damage() * 0.9


