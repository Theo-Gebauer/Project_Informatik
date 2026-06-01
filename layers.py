import global_var
from inventory import Inventory

class Layer:
    def __init__(self, layer):
        self.layer = layer
        self.effect = None
        self.effect_duration = 0
        self.effect_timer = 0
        self.potion_slot = Inventory(1, 1, 420, global_var.absolutey - self.layer * 140 - 110)
        self.potion_used = False
        
    def update(self):
        self.potion_slot.move(0, global_var.scroll_y)
        if not self.potion_slot.empty(0, 0):
            if self.potion_slot.item_slot[0][0].type == 'potion':
                if not self.potion_used:
                    for effect, value in self.potion_slot.item_slot[0][0].effects.items():
                        self.effect_duration = value*100 + 200
                        self.effect = effect
                if self.effect_timer < self.effect_duration:
                    self.effect_timer += 1
                    self.potion_slot.item_slot[0][0].fill_level(1 - self.effect_timer/self.effect_duration)
                    self.potion_used = True
                else:
                    self.potion_used = False
                    self.effect_timer = 0
                    self.effect_duration = 0
                    self.potion_slot.del_item(0, 0)

        
    def mouse(self, button, pos):
        if not self.potion_slot.empty(0, 0):
            if not self.potion_slot.item_slot[0][0].type == 'potion':
                self.potion_slot.mouse(button, pos)
        else:
            self.potion_slot.mouse(button, pos)

    def draw(self, screen):
        self.potion_slot.draw(screen)