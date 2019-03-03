from Warriors.WarriorBase import WarriorBase
from Weapons.WeaponBase import WeaponBase

class Gnome(WarriorBase):
	def __init__(self, weapon, name):
		super(Gnome, self).__init__(weapon, name)
		self.hp = self.hp + 10

	def kick(self):
		return self.weapon.get_damage() * 1.4
		
gnome = Gnome(Hammer, Biba)
print(gnome.hp) 

class Hammer(WeaponBase):
	def __init__(self, min_damage, max_damage):
        self.min_damage = 4
        self.max_damage = 7