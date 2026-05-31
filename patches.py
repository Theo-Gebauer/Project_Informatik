import random
import global_var
from inventory import Inventory
from pgzero.actor import Actor
import pygame

class Patch:
    def __init__(self, x, y):
        self.seed_slot = Inventory(1, 1, x, y - 30)
        self.harvest_slot = Inventory(2, 1, x - 32, y - 30)
        self.growth = 0
        self.growth_delay = 0
        self.growing_actor = None

        self.actor = Actor('patch', center = (x, y), anchor = ('center', 'center'))

    def update(self):
        if not self.seed_slot.empty(0, 0) and self.growth <= 4:
            self.growing_actor = self.seed_slot.item_slot[0][0].actor
            if self.growth_delay > 0:
                self.growth_delay -= 1
            else:
                self.growth += 1
                self.growth_delay = self.seed_slot.item_slot[0][0].delay * random.uniform(0.9, 1.1)
        elif not self.growth_delay == 0 and self.seed_slot.empty(0, 0) and self.harvest_slot.empty(0, 0) and self.harvest_slot.empty(1, 0):
            self.growth = 0
            self.growth_delay =  0
        elif self.growth > 4 and not self.seed_slot.empty(0, 0):
            self.harvest_slot.add_item(0, 0, self.seed_slot.item_slot[0][0])
            self.harvest_slot.add_item(1, 0, self.seed_slot.item_slot[0][0])
            self.seed_slot.del_item(0, 0)
            if global_var.inventory_selected == self.seed_slot:
                self.seed_slot.mouse(1, (self.seed_slot.inventory_background[0][0].x, self.seed_slot.inventory_background[0][0].y))
        elif self.harvest_slot.empty(0, 0) and self.harvest_slot.empty(1, 0):
            self.growth = 0
            self.growth_delay = 0

    def mouse(self, button, pos):
        if self.growth <= 4: 
            self.seed_slot.mouse(button, pos)
        else:
            self.harvest_slot.mouse(button, pos)


    def draw(self, screen):
        self.actor.draw()
        if self.growth == 1:
            Actor('pflanze_1', midbottom = (self.actor.x, self.actor.y)).draw()
        elif self.growth == 2:
            Actor('pflanze_2', midbottom = (self.actor.x, self.actor.y)).draw()
            growing_item = pygame.image.load("images/" + self.growing_actor.image + ".png")
            growing_item_1 = pygame.transform.scale(growing_item, (32, 32))
            screen.surface.blit(growing_item_1, (self.actor.x + 25, self.actor.y - 165))
        elif self.growth == 3:
            Actor('pflanze_3', midbottom = (self.actor.x, self.actor.y)).draw()
            growing_item = pygame.image.load("images/" + self.growing_actor.image + ".png")
            growing_item_1 = pygame.transform.scale(growing_item, (48, 48))
            growing_item_2 = pygame.transform.scale(growing_item, (32, 32))
            screen.surface.blit(growing_item_1, (self.actor.x + 25, self.actor.y - 165))            
            screen.surface.blit(growing_item_2, (self.actor.x - 40, self.actor.y - 225))
        elif self.growth == 4:
            Actor('pflanze_4', midbottom = (self.actor.x, self.actor.y)).draw()
            growing_item = pygame.image.load("images/" + self.growing_actor.image + ".png")
            growing_item_1 = pygame.transform.scale(growing_item, (48, 48))         
            screen.surface.blit(growing_item_1, (self.actor.x - 65, self.actor.y - 235))         
            screen.surface.blit(growing_item_1, (self.actor.x - 65, self.actor.y - 335))
            screen.surface.blit(growing_item_1, (self.actor.x - 55, self.actor.y - 455))
            screen.surface.blit(growing_item_1, (self.actor.x + 25, self.actor.y - 235))               
            screen.surface.blit(growing_item_1, (self.actor.x + 25, self.actor.y - 345))         
            screen.surface.blit(growing_item_1, (self.actor.x + 35, self.actor.y - 460))
        elif self.growth > 4:
            Actor('pflanze_4', midbottom = (self.actor.x, self.actor.y)).draw()
            growing_item_1 = pygame.image.load("images/" + self.growing_actor.image + ".png")
            screen.surface.blit(growing_item_1, (self.actor.x - 65, self.actor.y - 235))         
            screen.surface.blit(growing_item_1, (self.actor.x - 65, self.actor.y - 335))
            screen.surface.blit(growing_item_1, (self.actor.x - 55, self.actor.y - 455))
            screen.surface.blit(growing_item_1, (self.actor.x + 25, self.actor.y - 235))               
            screen.surface.blit(growing_item_1, (self.actor.x + 25, self.actor.y - 345))         
            screen.surface.blit(growing_item_1, (self.actor.x + 35, self.actor.y - 460))

        if global_var.inventory_open:
            if self.growth <= 4:
                self.seed_slot.draw()
            else:
                self.harvest_slot.draw()