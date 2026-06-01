from pgzero.actor import Actor
import global_var
import random
import pygame
from layers import Layer


#vars
duration_day = 3600
background_night = pygame.image.load('images/hintergrund_nacht.png')
background_night.set_alpha(0)

#Actors
clouds = [
    Actor('cloud1', topleft=(0,global_var.max_height+ 10)),
    Actor('cloud2', topleft=(200,global_var.max_height+50)),
    Actor('cloud3', topleft=(500,global_var.max_height+25)),
    Actor('cloud4', topleft=(500,global_var.max_height+60))
]

tower = Actor('turm', midbottom=(global_var.WIDTH//2, global_var.HEIGHT)) 
background = Actor('hintergrund_tag', topleft=(0, global_var.absolutey - 1680), anchor=('left', 'bottom'))
for i in range(4):
    clouds[i].vx = i+1


layers = []
for i in range(8):
    layers.append(Layer(i))


#Methods
    #action on mouse
def mouse_tower(button,pos): 
    if button == 1 and global_var.button_pressed(pos, 975, -950 + global_var.absolutey, 125, 110):
        global_var.scene = 2
    elif button == 1 and global_var.button_pressed(pos, 665, -1230 + global_var.absolutey, 180, 100):
        global_var.scene = 3
    else:
        for layer in layers:
            layer.mouse(button, pos)

    #update
def update_tower():
    global duration_day

    background.y += global_var.scroll_y
    tower.y += global_var.scroll_y

    for cloud in clouds:
        if cloud.left <= global_var.WIDTH:
            cloud.left += cloud.vx
        else:
            cloud.left = -450
            cloud.vx = random.randint(1,3)
        cloud.y += global_var.scroll_y

    if duration_day > 0:
        duration_day -= 1
    else:
        duration_day = 3600

    for layer in layers:
        layer.update()
     
    #draw
def draw_tower(screen):
    background.draw()
    if global_var.darkness > 0:
        background_night.set_alpha(global_var.darkness)
        screen.surface.blit(background_night, (0, global_var.absolutey - 1680))

    for i in range(2,4):
        clouds[i].draw()
    tower.draw()
    for i in range(0,2):
        clouds[i].draw()

    for layer in layers:
        layer.draw(screen)
