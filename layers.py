import global_var
from inventory import Inventory
from pgzero.actor import Actor
import random

class Layer:
    def __init__(self, layer):
        self.layer = layer
        self.effect = {}
        self.effect_duration = 0
        self.effect_timer = 0
        self.potion_slot = Inventory(1, 1, 420, global_var.absolutey - self.layer * 140 - 110)
        self.potion_used = False
        self.pulse = False
        self.animation = Actor('animations/nothing', midbottom = (global_var.WIDTH // 2 - 40, global_var.absolutey - self.layer * 137 - 105))

        self.frames = {
            'fire': [
                "animations/fire_1",
                "animations/fire_2",
                "animations/fire_3",
                "animations/fire_4",
                "animations/fire_5",
                "animations/fire_6",
                "animations/fire_7"
            ]
        }
        
    def update(self):
        self.animation.y += global_var.scroll_y

        self.potion_slot.move(0, global_var.scroll_y)
        if not self.potion_slot.empty(0, 0):
            if self.potion_slot.item_slot[0][0].type == 'potion':

                if not self.potion_used:
                    for effect, value in self.potion_slot.item_slot[0][0].effects.items():
                        self.effect_duration = value*100 + 200
                        self.effect[effect] = self.potion_slot.item_slot[0][0].effects[effect]
                        if effect == 'pulse':
                            self.pulse = True

                if self.effect_timer < self.effect_duration:
                    global_var.pulse = False
                    self.effect_timer += 1
                    self.potion_slot.item_slot[0][0].fill_level(1 - self.effect_timer/self.effect_duration)
                    self.potion_used = True
                    self.animate()
                    if self.pulse:
                        if self.effect_timer % (1000 // self.effect['pulse']) == 0:
                            global_var.pulse = True

                else:
                    self.potion_used = False
                    self.effect_timer = 0
                    self.effect_duration = 0
                    self.potion_slot.del_item(0, 0)
                    self.animation.image = 'animations/nothing'
            else:                
                self.effect = {}

        else:
            self.effect = {}

    def animate(self):
        if self.effect_timer % 9 == 0:
            self.animation.image = self.frames['fire'][random.randint(0,6)]



        
    def mouse(self, button, pos):
        if not self.potion_slot.empty(0, 0):
            if not self.potion_slot.item_slot[0][0].type == 'potion':
                self.potion_slot.mouse(button, pos)
        else:
            self.potion_slot.mouse(button, pos)

    def draw(self, screen):
        self.potion_slot.draw(screen)
        self.animation.draw()