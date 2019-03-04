from Weapons import Weapon

class WarriorBase:
    def __init__(self, weapon, name):
        self.name = name
        self.weapon = weapon
        self.hp = 100 

    def kick(self):
        pass
    def __str__(self):
        return f"Name: {self.name}\nHP: {self.hp}\nRace: {type(self).__name__}\nWeapon: {type(self.weapon).__name__}"

class Elf(WarriorBase):
    def __init__(self):
        super(Elf, self).__init__(weapon, name)
        self.hp = self.hp - 10

    def kick(self):
        return self.weapon.get_damage() * 1.3
    
class Orc(WarriorBase):

    def __init__(self, weapon, name):
        super(Orc, self).__init__(weapon, name)
        self.hp = self.hp + 20

    def kick(self):
        return self.weapon.get_damage() * 0.9

class Human(WarriorBase):
    def __init__(self, weapon, name):
        super(Human, self).__init__(weapon, name)


    def kick(self):
        return self.weapon.get_damage()*1.2
