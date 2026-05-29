from pgzero.actor import Actor
import global_var
import random
import math


#Actors


#Classes
class Monster():
    def __init__(self, type, hp, speed, x, y):
        self.actor = Actor(type)
        self.actor.pos = (x,y)

        self.hp = hp
        self.speed = speed
        self.type = type
        self.layer = 0

    def move(self, dx, dy):
            distance = math.sqrt(dx**2 + dy**2)

            dx = dx / distance
            dy = dy / distance

            self.actor.x += dx * self.speed
            self.actor.y += dy * self.speed + global_var.scroll_y


    def draw(self):
        self.actor.draw()

    def dmg(self, dmg):
        self.hp -= dmg

    def is_dead(self):
        return self.hp <= 0