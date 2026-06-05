from monster import Monster
import global_var
import random

class WaveManager:

    def __init__(self):
        self.wave = 0
        self.monsters = []
        self.difficulty = 0
        self.spawn_delay = 60
        self.path = [ 
                    (740, 890), (830, 730),
                    (615, 730), (500, 590),
                    (740, 590), (830, 450),
                    (615, 450), (500, 315),
                    (710, 315), (830, 180),
                    (615, 180), (500, 40),
                    (710, 40), (830, -100),
                    (615, -100), (500, -240)
                    ]

    def update(self):
        self.spawn_delay -= 1

        #spawning monsters
        if self.spawn_delay < 0:

            if self.difficulty > 0:
                difficulty_monster = random.randint(0, self.difficulty) % (len(global_var.all_monsters) - 1)

                properties_monster = global_var.all_monsters[difficulty_monster]

                monster = Monster(
                    properties_monster['image'], 
                    properties_monster['hp'] + 0.05 * self.wave * properties_monster['hp'], 
                    properties_monster['speed'] + 0.01 * self.wave * properties_monster['hp'], 
                    global_var.absolutex - 200, global_var.absolutey - 30, 
                    properties_monster['loot'],
                    self.path
                    )
                
                self.monsters.append(monster)

                self.difficulty -= difficulty_monster + 1

            self.spawn_delay = 90

        for monster in self.monsters:
            monster.move()

        #removing dead monsters
        self.monsters = [
            monster 
            for monster in self.monsters
            if not monster.is_dead()
        ]

    def next_wave(self):
        self.wave += 1
        self.difficulty = self.wave * 3 - 2

    def draw(self, screen):
        if global_var.scene == 1:
            for monster in self.monsters:
                monster.draw(screen)

    def ended(self): #returns whether all monsters are dead and there are no more to comme in current wave
        return len(self.monsters) == 0 and self.difficulty <= 0