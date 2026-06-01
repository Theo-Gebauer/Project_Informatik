import random
import global_var
from inventory import Inventory
from pgzero.actor import Actor
import pygame
from items import Item

class Brew_potions():
    def __init__(self, x, y):
        self.potion_slot = Inventory(1, 1, x, y)
        self.ingredients_slot = Inventory(1, 2, x, y - 32)
        self.button_actor = Actor('alchemy/brew_button', center = (x, y + 200), anchor = ('center', 'center'))

    def mouse(self, button, pos):
        if button == 1 and global_var.button_pressed(pos, self.button_actor.x, self.button_actor.y, 140, 40) and (not self.ingredients_slot.empty(0, 0) or not self.ingredients_slot.empty(0, 1)):
            
            possible_effects = {}
            for effect in global_var.all_effects:
                possible_effects[effect] = 0

            for i in range(len(self.ingredients_slot.item_slot[0])):
                if not self.ingredients_slot.item_slot[0][i] == 0:
                    if self.ingredients_slot.item_slot[0][i].type == 'ingredient':
                        for effect, value in self.ingredients_slot.item_slot[0][i].effects.items():
                            possible_effects[effect] += value

            max_value = 'poison'
            for effect, value in possible_effects.items():
                if value > possible_effects[max_value]:
                    max_value = effect
            
            if possible_effects[max_value] > 0:
                resulting_effect = {}
                resulting_effect[max_value] = possible_effects[max_value]
                self.potion_slot.item_slot[0][0] = Item('potion', 'potion', 0, None, resulting_effect)

                for i in range(len(self.ingredients_slot.item_slot[0])):
                    if self.ingredients_slot == global_var.inventory_selected:
                        self.ingredients_slot.mouse(1, (self.ingredients_slot.inventory_background[0][i].x, self.ingredients_slot.inventory_background[0][i].y))                
                    if not self.ingredients_slot.empty(0, i):
                        if self.ingredients_slot.item_slot[0][i].type == 'ingredient':
                            self.ingredients_slot.del_item(0, i)

        elif self.potion_slot.empty(0, 0):
            self.ingredients_slot.mouse(button, pos)
        else:
            self.potion_slot.mouse(button, pos)
                

    def draw(self, screen):
        if global_var.inventory_open:
            if self.potion_slot.empty(0, 0):
                self.ingredients_slot.draw(screen)
                self.button_actor.draw()
            else:
                self.potion_slot.draw(screen)
