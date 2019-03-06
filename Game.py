from Weapons import *
from Warriors import *
from random import randint
from time import sleep


sword = Sword()
human = Human(sword,"Ilya")
axe = Axe()
orc1 = Orc(axe, 'Lolik')


class FightField:
    def fight(self, fighter_1, fighter_2):
        while True:
            rand_kick = randint(1, 2)
            if rand_kick == 1:
                fighter_2.hp = fighter_2.hp - fighter_1.kick()
                print(f'{type(fighter_1).__name__} HP: {round(fighter_1.hp, 1)} kicked {type(fighter_2).__name__} HP: {round(fighter_2.hp, 1)}')
                sleep(1)
            elif rand_kick == 2:
                fighter_1.hp = fighter_1.hp - fighter_2.kick()
                print(f'{type(fighter_2).__name__} HP: {round(fighter_2.hp, 1)} kicked {type(fighter_1).__name__} HP: {round(fighter_1.hp, 1)}')
                sleep(1)

            if fighter_1.hp < 0:
                print(f'{type(fighter_2).__name__} Win !!!')
                return
            elif fighter_2.hp < 0:
                print(f'{type(fighter_1).__name__} Win !!!')
                return

fighting = FightField()
fighting.fight(orc1, human)





