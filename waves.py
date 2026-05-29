from monster import Monster
import global_var


class WaveManager:

    def __init__(self):
        self.wave = 1

        self.monsters = []

        self.monsters_to_spawn = 5

        self.spawn_timer = 0
        self.spawn_delay = 60

    def update(self):

        self.spawn_timer += 1

        #spawning
        if self.monsters_to_spawn > 0:

            if self.spawn_timer >= self.spawn_delay:
                hp = 50 + self.wave * 20
                speed = self.wave * 1.5

                monster = Monster("worm", hp, speed, global_var.absolutex, global_var.absolutey - 50)

                self.monsters.append(monster)

                self.monsters_to_spawn -= 1
                self.spawn_timer = 0

        #moving monsters
        for monster in self.monsters:
            if monster.actor.x > global_var.absolutex + 720 and monster.layer % 2 == 0:
                monster.move(3,-3)
            elif monster.actor.x < global_var.absolutex + 610 and monster.layer % 2 == 1:
                monster.move(-3,-3)
            elif monster.layer % 2 == 0:
                monster.move(3,0)
            else:
                monster.move(-3,0)

        #removing dead monsters
        self.monsters = [
            monster 
            for monster in self.monsters
            if not monster.is_dead()
        ]

        # Neue Welle
        if (self.monsters_to_spawn <= 0 and len(self.monsters) == 0):
            self.next_wave()
            print("new Wave")

    def next_wave(self):
        self.wave += 1
        self.monsters_to_spawn = 5 + self.wave * 3

    def draw(self):
        for monster in self.monsters:
            monster.draw()