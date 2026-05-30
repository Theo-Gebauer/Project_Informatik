from pgzero.actor import Actor
import global_var
import random
import math


#Actors


#Classes
class Monster():
    def __init__(self, image, hp, speed, x, y, type, waypoints):
        self.hp = hp
        self.speed = speed
        self.type = type
        self.layer = 0
        self.type = type
        self.waypoints = waypoints
        self.next_waypoint = 0

        self.actor = Actor(image)
        self.actor.pos = (x,y)

    def move(self):
        target_x, target_y = self.waypoints[self.next_waypoint]

        dx = target_x - self.actor.x
        dy = target_y + global_var.absolutey - 930 - self.actor.y

        distance = math.hypot(dx, dy)
        if distance > self.speed:

            dx /= distance
            dy /= distance

            self.actor.x += dx * self.speed
            self.actor.y += dy * self.speed + global_var.scroll_y

        elif self.next_waypoint + 1 < len(self.waypoints):
            self.next_waypoint += 1
        else:
            global_var.game_lost = True


    def draw(self):
        self.actor.draw()

    def dmg(self, dmg):
        self.hp -= dmg

    def is_dead(self):
        return self.hp <= 0