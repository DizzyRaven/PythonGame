class WarriorBase:
    def __init__(self, hp_plus, weapon, name):
        self.name = name
        self.weapon = weapon
        self.hp = 100 + hp_plus

    def kick(self):
        pass
