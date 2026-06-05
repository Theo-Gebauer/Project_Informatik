import global_var
from inventory import Inventory
from pgzero.actor import Actor

class Layer:
    def __init__(self, layer):
        self.layer = layer
        self.effect = {}
        self.effect_duration = 0
        self.effect_timer = 0
        self.potion_used = False
        self.pulse = False
        self.animation_effect = None

        if layer == 0:
            self.layer = -0.2
        self.potion_slot = Inventory(1, 1, 420, global_var.absolutey - self.layer * 140 - 110)
        self.animation = Actor('animations/nothing', midbottom = (global_var.WIDTH // 2 - 40, global_var.absolutey - self.layer * 137 - 105))
        
        self.layer = layer
        
        self.frame = 0
        self.frames = {
            'fire': [
                "animations/fire_1",
                "animations/fire_2",
                "animations/fire_3",
                "animations/fire_4",
                "animations/fire_5",
                "animations/fire_6",
                "animations/fire_7"
            ],
            'pulse': [
                "animations/nothing",
                "animations/pulse_2",
                "animations/pulse_3",
                "animations/pulse_4",
                "animations/pulse_5",
                "animations/pulse_6",
                "animations/pulse_7"
            ],
            'ice': [
                "animations/ice_1",
                "animations/ice_2",
                "animations/ice_3",
                "animations/ice_4",
                "animations/ice_5",
                "animations/ice_6",
                "animations/ice_7",
                "animations/ice_8"
            ],
            'slow': [
                "animations/slow_1"
            ],
            'poison': [
                "animations/poison_1",
                "animations/poison_2",
                "animations/poison_3"
            ],
        }
        

    def update(self):
        self.animation.y = global_var.absolutey - self.layer * 137 - 105
        self.potion_slot.inventory_background[0][0].y = global_var.absolutey - self.layer * 140 - 110
        self.potion_slot.update()

        if not self.potion_slot.empty(0, 0): #determines effect on itself/updates duration from this effect
            if self.potion_slot.item_slot[0][0].type == 'potion':

                if not self.potion_used:
                    for effect_name, value in self.potion_slot.item_slot[0][0].effects.items():
                        self.effect_duration = value * 100 + 200
                        self.effect[effect_name] = self.potion_slot.item_slot[0][0].effects[effect_name]
                        self.animation_effect = effect_name
                        if effect_name == 'pulse':
                            self.pulse = True
                        else:
                            self.pulse = False

                if self.effect_timer < self.effect_duration:
                    global_var.pulse[self.layer] = False
                    self.effect_timer += 1
                    self.potion_slot.item_slot[0][0].fill_level(1 - self.effect_timer/self.effect_duration)
                    self.potion_used = True
                    self.animate()
                    if self.pulse:
                        if self.effect_timer % (1000 // self.effect['pulse']) == 0:
                            global_var.pulse[self.layer] = True

                else:
                    self.frame = 0
                    self.animation_effect = None
                    self.potion_used = False
                    self.effect_timer = 0
                    self.effect_duration = 0
                    self.potion_slot.del_item(0, 0)
                    self.animation.image = 'animations/nothing'

            else:                
                self.effect = {}

        else:
            self.effect = {}

    def animate(self): #animates the effect of a potion on this layer
        if self.pulse:
            if self.effect_timer % (1000 // self.effect['pulse']) == 0 or len(self.frames[self.animation_effect]) - 1 > self.frame > 0:
                self.frame += 1
            elif self.effect_timer % 10 == 0:
                self.frame = 0
        else:
            if self.effect_timer % 10 == 0:
                self.frame += 1
                if self.frame  % len(self.frames[self.animation_effect]) == 0:
                    self.frame = 0

        self.animation.image = self.frames[self.animation_effect][self.frame]

        
    def mouse(self, button, pos):
        if not self.potion_slot.empty(0, 0):
            if not self.potion_slot.item_slot[0][0].type == 'potion': #locks slot from being changed while a potion is in it
                self.potion_slot.mouse(button, pos)
        else:
            self.potion_slot.mouse(button, pos)

    def draw(self, screen):
        self.potion_slot.draw(screen)
        self.animation.draw()