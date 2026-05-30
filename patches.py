import random
import global_var
from inventory import Inventory
from pgzero.actor import Actor

class Patch:
    def __init__(self, x, y):
        self.seed_slot = Inventory(1, 1, x, y - 30)
        self.harvest_slot = Inventory(2, 1, x - 32, y - 30)
        self.growth = 0
        self.growth_delay = 0

        self.actor = Actor('patch', center = (x, y), anchor = ('center', 'center'))

    def update(self):
        if not self.seed_slot.item_slot[0][0] == 0 and self.growth <= 4:
            print(self.growth_delay)
            if self.growth_delay > 0:
                self.growth_delay -= 1
            else:
                self.growth += 1
                self.growth_delay = self.seed_slot.item_slot[0][0].delay * random.uniform(0.9, 1.1)
        elif self.growth > 4:
            self.seed_slot.del_item(0, 0)

    def mouse(self, button, pos):
        if self.growth <= 4: 
            self.seed_slot.mouse(button, pos)
        else:
            self.harvest_slot.mouse(button, pos)


    def draw(self):
        self.actor.draw()
        if global_var.inventory_open:
            if self.growth <= 4:
                self.seed_slot.draw()
            else:
                self.harvest_slot.draw()