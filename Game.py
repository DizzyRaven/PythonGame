from Weapons import *
from Warriors import *


sword = Sword()
human = Human(sword,"Ilya")
axe = Axe()
orc = Orc(axe, 'Stepan')

print (human)

print (human.kick())

print (orc)

print (orc.kick())