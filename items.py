from pgzero.actor import Actor
import global_var
import random
import pygame


class Item():
    def __init__(self, name, type, delay, image, standart_effect):
        self.value = 0
        self.discovered_effects = {}

        if type == 'ingredient':
            self.effects = self.generate_effects(standart_effect)
            self.name = name
            self.type = type
            self.delay = delay

            self.actor = Actor(image)
            for effect, value in self.effects.items():
                self.value += value

        if type == 'potion':
            self.vis_height = 28
            self.name = name
            self.type = type
            self.delay = delay
            self.effects = standart_effect
            self.actor = Actor('items/empty_bottle')
            self.liquid_base = pygame.image.load("images/items/liquid.png").convert_alpha()
            self.liquid = self.liquid_base.copy()
            for effect, value in self.effects.items():                
                self.discovered_effects[effect] = value
                color = global_var.effect_to_color.get(effect, (200, 200, 200))
                self.liquid.fill(color, special_flags=pygame.BLEND_MULT)
                self.value = value * 2


    def generate_effects(self, standart_effect): #generates 1-3 (if the same is selected twice the second one willbe saved) random effects

        effects = {}

        for i in range(random.randint(2,3)):
            if standart_effect is not None:
                effects[standart_effect] = round(random.uniform(5, 10), 1)
                standart_effect = None
            else:
                effects[global_var.all_effects[random.randint(0 , len(global_var.all_effects) - 1)]] = round(random.uniform(5, 10), 1)

        return(effects)
    
    def fill_level(self, fill_level): #returns fill level on this potion
        self.vis_height = int(self.liquid.get_height() * fill_level)
    
    def draw(self, x, y, screen):
        self.actor.center = (x, y)
        self.actor.draw()
        
        if self.type == 'potion': #draws liquid inside a potion
            rect = pygame.Rect(
                0,
                self.liquid.get_height() - self.vis_height,
                self.liquid.get_width(),
                self.vis_height
                )
            screen.surface.blit(self.liquid, (x - 14, y - 9 + (self.liquid.get_height() - self.vis_height)), rect)