from monster import Monster
import global_var

class WaveManager:

    def __init__(self):
        self.wave = 0

        self.monsters = []

        self.monsters_to_spawn = 0

        self.spawn_delay = 60

    def update(self):
        self.spawn_delay -= 1

        #spawning
        if self.monsters_to_spawn > 0:

            if self.spawn_delay < 0:
                hp = 50 + self.wave * 20
                speed = self.wave * 0.1 + 1

                dead_worm = global_var.all_ingredients['dead_worm']

                monster = Monster("worm", hp, speed, global_var.absolutex - 200, global_var.absolutey - 30, 'monster/worm', dead_worm,[ 
                    (740, 890), (830, 730),
                    (615, 730), (500, 590),
                    (740, 590), (830, 450),
                    (615, 450), (500, 315),
                    (710, 315), (830, 180),
                    (615, 180), (500, 40),
                    (710, 40), (830, -100),
                    (615, -100), (500, -240)
                    ])
                
                self.monsters.append(monster)

                self.monsters_to_spawn -= 1
                self.spawn_delay = 90

        #moving monsters
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
        self.monsters_to_spawn = self.wave * 3

    def draw(self):
        if global_var.scene == 1:
            for monster in self.monsters:
                monster.draw()

    def ended(self):
        return len(self.monsters) == 0 and self.monsters_to_spawn == 0