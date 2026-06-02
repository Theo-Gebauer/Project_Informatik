from pgzero.actor import Actor
import global_var
import random
import pygame
from pgzero.builtins import Rect


class Item():
    def __init__(self, name, type, delay, image, standart_effect):
        self.value = 1
        self.hovered = False

        if type == 'ingredient':
            effects = self.generate_effects(standart_effect)
            self.effects = effects
            self.name = name
            self.type = type
            self.delay = delay

            self.actor = Actor(image)

        elif type == 'potion':
            self.vis_height = 28
            self.name = name
            self.type = type
            self.delay = delay
            self.effects = standart_effect
            self.actor = Actor('items/empty_bottle')
            self.liquid_base = pygame.image.load("images/items/liquid.png").convert_alpha()
            self.liquid = self.liquid_base.copy()
            for effect, value in self.effects.items():
                color = global_var.effect_to_color.get(effect, (200, 200, 200))
                self.liquid.fill(color, special_flags=pygame.BLEND_MULT)
            self.value = 2

        for effect, value in self.effects.items():
            self.value *= value

    def generate_effects(self, standart_effect):    

        effects = {}

        for i in range(random.randint(2,3)):
            if standart_effect is not None:
                effects[standart_effect] = round(random.uniform(5, 10), 1)
                standart_effect = None
            else:
                effects[global_var.all_effects[random.randint(0 , len(global_var.all_effects) - 1)]] = round(random.uniform(5, 10), 1)

        return(effects)
    
    def fill_level(self, fill_level):
        self.vis_height = int(self.liquid.get_height() * fill_level)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.actor.collidepoint(mouse_pos):
            self.hovered = True
        else:
            self.hovered = False
    
    def draw(self, x, y, screen):
        self.actor.center = (x, y)
        self.actor.draw()

        if self.hovered:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            i = 0            
            for prop, value in self.effects.items():
                i += 1 

            screen.draw.filled_rect(
                Rect(mouse_x - 100, mouse_y  - i * 20 - 5, 100, i * 20),
                (30, 30, 30)
            )

            screen.draw.text(
                self.name,
                (mouse_x - 20, mouse_y - 20),
                color="white"
            )
            
            y_offset = 0
            for prop, value in self.effects.items():
                screen.draw.text(
                    f"{prop}: {value}",
                    (mouse_x - 20, mouse_y - 20 + y_offset),
                    color="white"
                )
                y_offset += 20

        if self.type == 'potion':
            rect = pygame.Rect(
                0,
                self.liquid.get_height() - self.vis_height,
                self.liquid.get_width(),
                self.vis_height
                )
            screen.surface.blit(self.liquid, (x - 14, y - 9 + (self.liquid.get_height() - self.vis_height)), rect)
