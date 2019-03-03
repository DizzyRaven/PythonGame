from Warriors.WarriorBase import WarriorBase
class Elf(WarriorBase):
    def __init__(self):
        super(Elf, self).__init__(weapon, name)
        self.hp = self.hp - 10
elf = Elf('Sword', 'Eleanor')
print(elf.hp)