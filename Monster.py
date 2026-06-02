from pgzero.actor import Actor
import global_var
import random
import math


#Actors


#Classes
class Monster():
    def __init__(self, image, hp, speed, x, y, type, loot, waypoints):
        self.hp = hp
        self.speed = speed
        self.type = type
        self.layer = 0
        self.type = type
        self.waypoints = waypoints
        self.next_waypoint = 0
        self.loot = loot

        self.actor = Actor(image, pos=(x, y))

        self.effects = {
            'poison': {
                'duration': 0,
                'dmg': 0,
                'timer': 0,
                'timer_apply': 1
                },
            'fire': {
                'duration': 0,
                'dmg': 0,
                'timer': 0,
                'timer_apply': 1
                },
            'ice': {
                'duration': 0,
                'dmg': 0,
                'speed_decrease': 0,
                'timer': 0,
                'timer_apply': 1
                },
            'slow': {
                'duration': 0,
                'dmg': 0,
                'speed_decrease': 0,
                'timer': 0,
                'timer_apply': 1
                }
        }

    def move(self):
        target_x, target_y = self.waypoints[self.next_waypoint]

        dx = target_x - self.actor.x
        dy = target_y + global_var.absolutey - 930 - self.actor.y

        distance = math.hypot(dx, dy)

        while (self.effects['ice']['speed_decrease'] + self.effects['slow']['speed_decrease']) >= self.speed - 0.5:
            if self.effects['ice']['speed_decrease']  > 0:
                self.effects['ice']['speed_decrease'] = self.effects['ice']['speed_decrease'] - 0.05
            if self.effects['slow']['speed_decrease']  > 0:
                self.effects['slow']['speed_decrease'] = self.effects['slow']['speed_decrease'] - 0.05

        if distance > (self.speed - (self.effects['ice']['speed_decrease'] + self.effects['slow']['speed_decrease'])):

            dx /= distance
            dy /= distance
    
            self.actor.x += dx * (self.speed - (self.effects['ice']['speed_decrease'] + self.effects['slow']['speed_decrease']))
            self.actor.y += dy * (self.speed - (self.effects['ice']['speed_decrease'] + self.effects['slow']['speed_decrease'])) + global_var.scroll_y

        elif self.next_waypoint + 1 < len(self.waypoints):
            self.next_waypoint += 1
        else:
            global_var.game_lost = True

        if self.next_waypoint % 2 == 0 and self.actor.x >= 480:
            if not global_var.layers[self.next_waypoint // 2].effect == {}:
                self.effect_layer(global_var.layers[self.next_waypoint // 2].effect)
                self.effect_apply()

    def effect_layer(self, effect):
        for effect_name, strength in effect.items():
            if effect_name == 'poison':
                self.effects[effect_name]['duration'] = strength * 200
                self.effects[effect_name]['dmg'] = strength * 0.02
                self.effects[effect_name]['timer_apply'] =  100 // strength
            elif effect_name == 'fire':
                self.effects[effect_name]['duration'] = strength * 20
                self.effects[effect_name]['dmg'] = strength * 0.1 + 1
                self.effects[effect_name]['timer_apply'] =  100 // strength
                self.effects['ice']['duration'] = 0
            elif effect_name == 'ice':
                self.effects[effect_name]['duration'] = strength * 20
                self.effects[effect_name]['dmg'] = strength * 0.05
                self.effects[effect_name]['timer_apply'] =  100 // strength
                self.effects[effect_name]['speed_decrease'] = strength * 0.02
                self.effects['fire']['duration'] = 0
                self.effects['slow']['duration'] = strength * 10
            elif effect_name == 'slow':
                self.effects[effect_name]['duration'] = strength * 200
                self.effects[effect_name]['speed_decrease'] = strength * 0.1
            elif effect_name == 'pulse':
                if global_var.pulse == True:
                    self.dmg(strength * 2)

    def effect_apply(self):
        for effect_name, properties in self.effects.items():
            print(f'{effect_name} | {properties}')
            if properties['duration'] > properties['timer']:
                properties['timer'] += 1
                if properties['timer'] % properties['timer_apply'] == 0:
                    print(f'{self.hp}|')
                    self.dmg(properties['dmg'])
                    print(self.hp)
            else:
                properties['duration'] = 0
                properties['timer'] = 0
            if effect_name == 'slow' or effect_name == 'ice':
                if properties['duration'] <= properties['timer']:
                    self.effects[effect_name]['speed_decrease'] = 0

    def draw(self):
        self.actor.draw()

    def dmg(self, dmg):
        self.hp -= dmg

    def is_dead(self):
        return self.hp <= 0